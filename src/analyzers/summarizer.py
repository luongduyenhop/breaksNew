import os
import json
import threading
import time

import requests
from google import genai
from typing import List
from src.filters.relevance import (
    comment_insight_score,
    expert_voice_score,
    incident_severity_score,
    is_major_incident,
    rank_comments,
)
from src.models.raw_item import RawItem

# Current Gemini model ids, most preferred first. gemini-3.8-flash is
# the current Flash model (GA 2026-09-02). The Gemini 2.5 family has
# been limited to past users since 2026-09-18, so fresh AI Studio API
# keys cannot call gemini-2.5-flash — it stays last as a legacy option
# for older keys. GEMINI_MODEL env still takes precedence.
DEFAULT_MODELS = [
    "gemini-3.8-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash-lite",
    "gemini-2.5-flash",
]

TOP_ITEMS_FOR_PROMPT = 20
VN_PROMPT_MIN = 8
# Hard wall-clock budget for the WHOLE Gemini phase (all candidate
# models together). Luong's rule (2026-10-31): if Gemini has not
# produced a report within 2 minutes, stop waiting on it and switch to
# the OpenCode Zen chain — a slow Gemini must not hold the briefing
# hostage. Override with GEMINI_TIME_BUDGET_SECS.
GEMINI_TIME_BUDGET_SECS = 120
# Major incidents are high-value but must not flood the briefing: at
# most this many gate-passing incident items reach the prompt per day.
INCIDENT_PROMPT_MAX = 3

# OpenCode Zen fallback (OpenAI-compatible). Free ids rotate often —
# override with the OPENCODE_MODELS env (comma-separated) instead of
# editing code when the roster changes.
ZEN_BASE_URL = "https://opencode.ai/zen/v1"
ZEN_DEFAULT_MODELS = [
    "deepseek-v4.1-flash-free",
    "glm-5.3-flash-free",
    "mimo-v2.6-flash-free",
]
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
# Free lineup verified live on 2026-11-01 via the public models API.
# Free ids rotate over time; OPENROUTER_MODELS overrides, and the
# openrouter/free router id (auto-picks an available free model)
# stays last as a catch-all.
OPENROUTER_DEFAULT_MODELS = [
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    "google/gemma-4-31b-it:free",
    "openrouter/free",
]
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
# Groq free tier caps large models by tokens/minute (llama-3.3-70b:
# 12K TPM, 100K tokens/day), so Groq receives the COMPACT payload
# (see _build_payload) and a single strong default model.
GROQ_DEFAULT_MODELS = ["llama-3.3-70b-versatile"]
GROQ_COMPACT_ITEMS = 10
FALLBACK_WARNING = (
    "> ⚠️ **Cảnh báo:** Bản tin hôm nay là bản tổng hợp tự động (fallback) vì "
    "Gemini không chạy được — nội dung dưới đây là danh sách nguồn đã lọc theo "
    "điểm liên quan, chưa có lớp phân tích sâu. Kiểm tra GEMINI_API_KEY / "
    "GEMINI_MODEL trong GitHub Secrets.\n\n"
)


class MarketBriefingSynthesizer:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key) if self.api_key else None
        self.used_fallback = False

    def _ranked(self, items: List[RawItem]) -> List[RawItem]:
        """Highest relevance first — never raw collection order."""
        return sorted(items, key=lambda i: i.relevance_score, reverse=True)

    def _select_for_prompt(self, ranked: List[RawItem]) -> List[RawItem]:
        """Top-N for the prompt, with a soft floor for Vietnam-market items.

        Global sources are far more numerous, so a pure score ranking can
        crowd out VN items entirely — yet the reader's decisions happen in
        the Vietnamese market. Guarantee at least VN_PROMPT_MIN VN items
        (when that many cleared the relevance bar), swapping them in for
        the lowest-scored non-VN selections.
        """
        selected = list(ranked[:TOP_ITEMS_FOR_PROMPT])
        vn_in = [i for i in selected if i.region == "VN"]
        if len(vn_in) >= VN_PROMPT_MIN:
            return self._cap_incidents(selected, ranked)
        vn_pool = [
            i for i in ranked[TOP_ITEMS_FOR_PROMPT:] if i.region == "VN"
        ]
        need = VN_PROMPT_MIN - len(vn_in)
        for vn_item in vn_pool[:need]:
            for idx in range(len(selected) - 1, -1, -1):
                if selected[idx].region != "VN":
                    selected[idx] = vn_item
                    break
        selected = sorted(selected, key=lambda i: i.relevance_score, reverse=True)
        return self._cap_incidents(selected, ranked)

    @staticmethod
    def _cap_incidents(selected: List[RawItem], ranked: List[RawItem]) -> List[RawItem]:
        """At most INCIDENT_PROMPT_MAX major incidents reach the prompt.

        Excess incidents (lowest-scored first) are swapped for the best
        unselected non-incident items, keeping the selection size stable.
        """
        incidents = [i for i in selected if is_major_incident(i)]
        if len(incidents) <= INCIDENT_PROMPT_MAX:
            return selected
        excess = incidents[INCIDENT_PROMPT_MAX:]
        replacements = [
            i for i in ranked if i not in selected and not is_major_incident(i)
        ]
        for old in excess:
            selected.remove(old)
            if replacements:
                selected.append(replacements.pop(0))
        return sorted(selected, key=lambda i: i.relevance_score, reverse=True)

    def _build_payload(self, ranked: List[RawItem], compact: bool = False):
        """JSON payload for the synthesis prompt.

        compact=True builds the trimmed variant for providers with tight
        per-minute token caps (Groq free tier: 12K TPM): fewer items,
        shorter previews, fewer and shorter comments — sized to stay
        around 6-7K input tokens so input + report fit under the cap.
        """
        selected = self._select_for_prompt(ranked)
        if compact:
            selected = selected[:GROQ_COMPACT_ITEMS]
        preview_limit = 400 if compact else 1000
        comment_limit = 2 if compact else 4
        comment_chars = 350 if compact else 0
        payload = []
        for item in selected:
            comments_data = [
                {
                    "author": c.author,
                    "votes": c.votes,
                    "insight_score": round(comment_insight_score(c.text), 1),
                    "text": c.text[:comment_chars] if comment_chars else c.text,
                }
                for c in rank_comments(item.top_comments, limit=comment_limit)
            ]
            payload.append({
                "title": item.title,
                "source": item.source_name,
                "type": item.source_type,
                "region": item.region,
                "url": item.url,
                "relevance_score": item.relevance_score,
                "expert_voice_score": round(expert_voice_score(item), 1),
                "is_major_incident": is_major_incident(item),
                "incident_severity": round(incident_severity_score(item), 1),
                "matched_topics": item.matched_topics,
                "content_preview": item.summary_text[:preview_limit],
                "top_comments": comments_data,
            })
        return payload

    def _render_prompt(self, payload) -> str:
        context_json = json.dumps(payload, ensure_ascii=False, indent=2)
        return f"""
        Bạn là chuyên gia phân tích định hướng nghề nghiệp IT cho lập trình viên Việt Nam.
        Dưới đây là các bài viết / video / thảo luận ĐÃ ĐƯỢC LỌC theo điểm liên quan,
        kèm BÌNH LUẬN của cộng đồng. Mỗi bình luận có `insight_score` — điểm giá trị
        định hướng do hệ thống chấm (bình luận của người trong nghề giải thích ngành
        đang đi về đâu, cần học gì, tư duy thế nào sẽ có điểm cao):

        {context_json}

        NGƯỜI ĐỌC THỰC SỰ MUỐN GÌ — đây là trọng tâm của bản tin:
        - Không phải tin tức IT nói chung. Người đọc muốn ĐỊNH HƯỚNG: ngành IT hiện
          nay đang đi theo hướng nào, người học IT bây giờ cần học NHỮNG GÌ (kỹ năng
          và CÔNG NGHỆ cụ thể), áp dụng như thế nào vào học tập/công việc, và cần
          thay đổi TƯ DUY ra sao.
        - Nguồn giá trị nhất là các bình luận dài của người trong nghề (insight_score
          cao): họ nói thẳng điều bài viết/video không nói. Ưu tiên khai thác chúng.
        - ƯU TIÊN TIẾNG NÓI CHUYÊN GIA: mỗi mục có `expert_voice_score` — điểm cho
          thấy tác giả/người nói là senior, tech lead, PM, engineering manager hay
          người nhiều năm kinh nghiệm. Lời khuyên từ những người này phải được ưu
          tiên trích và phân tích trước tin tức thông thường. Khi nhận diện được
          vai trò (từ tiêu đề/nội dung), PHẢI ghi rõ: "theo một tech lead...",
          "góc nhìn của engineering manager...", "một senior 10 năm kinh nghiệm...".
        - PHẠM VI ĐỊA LÝ: mỗi mục có trường `region` (VN = Việt Nam, GLOBAL = quốc
          tế). Người đọc ra quyết định ở thị trường Việt Nam: tin VN là trọng tâm,
          xu hướng quốc tế chỉ có giá trị khi nói rõ nó áp dụng được gì vào bối
          cảnh VN (tuyển dụng, lương, văn hóa công ty, nhu cầu khách hàng).
        - Mọi nhận định phải bám dữ liệu: nguồn/bình luận nào nói. Không bịa số liệu,
          không viết sáo rỗng kiểu "AI đang phát triển mạnh mẽ".

        QUY TẮC SONG NGỮ:
        - Phân tích, nhận định, lời khuyên: TIẾNG VIỆT trước, rõ ràng, thực chiến.
        - Trích dẫn nguyên văn tiếng Anh đắt giá: đặt ngay bên dưới dạng
          `> English reference: ...`.

        CẤU TRÚC BÁO CÁO BẮT BUỘC (đúng 6 mục; mục 6 có điều kiện):

        # BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT

        ## 1. HƯỚNG ĐI CỦA NGÀNH IT HIỆN NAY
        - Tách rõ hai phần:
          ### Tại Việt Nam
          - Các dịch chuyển từ nguồn region=VN: tuyển dụng/layoff, lương, nhu cầu
            kỹ năng ở thị trường VN.
          ### Trên thế giới (và ý nghĩa với Việt Nam)
          - Các dịch chuyển từ nguồn region=GLOBAL, mỗi ý PHẢI chốt một câu: điều
            này có ý nghĩa gì với dev Việt Nam.
        - Tổng cộng 3-5 dịch chuyển quan trọng nhất (AI thay đổi cách làm việc ra
          sao, tuyển dụng/layoff, vai trò dev đang biến đổi thế nào), mỗi ý kèm
          nguồn dẫn chứng. Nếu một phần thiếu dữ liệu thì nói rõ thay vì bịa.

        ## 2. NGƯỜI HỌC IT BÂY GIỜ CẦN HỌC GÌ
        - Kỹ năng cần học: liệt kê cụ thể, kèm vì sao và nguồn/bình luận nào nhắc tới.
        - Công nghệ cần học: liệt kê cụ thể (ngôn ngữ, framework, mảng AI/security/
          system...), phân biệt "đang là xu hướng thật" vs "chỉ là hype" nếu dữ liệu
          cho phép nhận định.

        ## 3. TƯ DUY & CÁCH ÁP DỤNG
        - Những thay đổi tư duy được cộng đồng nhắc nhiều nhất (vd: từ làm theo task
          sang hiểu business + cả hệ thống, kỹ năng làm việc với con người...).
        - Cách áp dụng cụ thể cho một dev nền Java/Spring Boot đang học thêm Python
          và network security: tuần này nên làm gì, tránh gì.

        ## 4. BÌNH LUẬN ĐỊNH HƯỚNG HAY NHẤT
        - Chọn 3-5 bình luận có insight_score cao nhất. Trích DÀI, giữ trọn ý chính
          (không cắt còn 1 dòng), kèm tác giả, số votes, thuộc video/bài nào (kèm link),
          và 1-2 câu vì sao bình luận này đáng đọc.

        ## 5. NGUỒN NÊN XEM / ĐỌC HÔM NAY
        - Các nguồn điểm liên quan cao nhất: tiêu đề + link + nhãn [VN] hoặc
          [Quốc tế], 2-3 câu tóm tắt luận điểm chính, góc nhìn nổi bật nhất từ
          bình luận, lý do được chọn. Ưu tiên nguồn có expert_voice_score cao.

        ## 6. SỰ CỐ CÔNG NGHỆ LỚN & BÀI HỌC NGHỀ NGHIỆP
        - CHỈ viết mục này khi dữ liệu có mục với `is_major_incident` = true
          (sự cố đã qua cổng nghiêm trọng: có CVE/CVSS cao/KEV/bị khai thác
          thực tế...). Nếu KHÔNG có mục nào như vậy, bỏ qua mục 6 hoàn toàn,
          không nhắc tới nó.
        - Với mỗi sự cố (tối đa 3): chuyện gì xảy ra trong 2-3 dòng (kèm mã
          CVE, điểm CVSS, trạng thái KEV/khai thác nếu dữ liệu có), quy mô
          ảnh hưởng, và quan trọng nhất là BÀI HỌC NGHỀ NGHIỆP: kỹ năng nào
          bỗng trở nên đắt giá (kiểm kê hệ thống, vá lỗi khẩn cấp, ứng phó
          sự cố, hardening, săn dấu hiệu xâm nhập...), nhu cầu nhân lực
          security thay đổi ra sao, và người đọc (dev Java/Spring Boot đang
          học Python/network security) nên làm hoặc học gì cụ thể trong
          tuần này liên quan đến sự cố. Không đăng lại tin tức thuần túy —
          chỉ lấy phần có giá trị định hướng nghề nghiệp.
        """

    def analyze_and_synthesize(self, items: List[RawItem]) -> str:
        ranked = self._ranked(items)
        prompt = self._render_prompt(self._build_payload(ranked))

        if not self.client:
            print("Gemini API skipped: No GEMINI_API_KEY provided.")
        else:
            candidate_models = []
            env_model = os.environ.get("GEMINI_MODEL")
            if env_model:
                candidate_models.append(env_model)
            candidate_models.extend(m for m in DEFAULT_MODELS if m not in candidate_models)

            budget_secs = self._gemini_budget_secs()
            deadline = time.monotonic() + budget_secs
            budget_exhausted = False
            for model_candidate in candidate_models:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    budget_exhausted = True
                    break
                report_text = self._try_model_with_timeout(
                    model_candidate, prompt, remaining
                )
                if report_text:
                    self.used_fallback = False
                    print(f"Gemini report generated with model: {model_candidate}")
                    return report_text

            if budget_exhausted:
                print(
                    f"Gemini time budget ({budget_secs:.0f}s) exhausted — "
                    "switching to fallback provider chains."
                )
            else:
                print("All Gemini models failed.")
        print("Trying OpenRouter fallback chain.")
        or_text = self._try_openrouter_chain(prompt)
        if or_text:
            self.used_fallback = False
            return or_text

        print("Trying Groq fallback chain (trimmed payload).")
        groq_prompt = self._render_prompt(self._build_payload(ranked, compact=True))
        groq_text = self._try_groq_chain(groq_prompt)
        if groq_text:
            self.used_fallback = False
            return groq_text

        print("Trying OpenCode Zen fallback chain.")
        zen_text = self._try_opencode_chain(prompt)
        if zen_text:
            self.used_fallback = False
            return zen_text

        print("All providers failed. Falling back to structured local report.")
        self.used_fallback = True
        return FALLBACK_WARNING + self._build_fallback_report(ranked)

    @staticmethod
    def _gemini_budget_secs() -> float:
        """Total wall-clock budget for the Gemini phase, in seconds."""
        raw = os.environ.get("GEMINI_TIME_BUDGET_SECS", "")
        try:
            value = float(raw)
            if value > 0:
                return value
        except (TypeError, ValueError):
            pass
        return float(GEMINI_TIME_BUDGET_SECS)

    def _try_model_with_timeout(self, model_name: str, prompt: str, timeout_secs: float):
        """Run one Gemini attempt under a hard wall-clock cap.

        The genai SDK calls carry no reliable per-request timeout, so a
        hung model could previously block the pipeline for many minutes.
        The attempt runs on a daemon thread; if it has not finished when
        the remaining Gemini budget runs out, it is abandoned (its result
        is discarded) and the caller moves on to the Zen chain.
        """
        outcome = {}

        def _run():
            try:
                outcome["text"] = self._try_model(model_name, prompt)
            except Exception as error:  # _try_model already guards, be safe
                print(f"Gemini attempt error with model {model_name}: {error}")
                outcome["text"] = None

        worker = threading.Thread(target=_run, daemon=True)
        worker.start()
        worker.join(timeout=max(0.1, timeout_secs))
        if worker.is_alive():
            print(
                f"Gemini attempt with model {model_name} exceeded the "
                f"remaining time budget ({timeout_secs:.0f}s) — abandoning it."
            )
            return None
        return outcome.get("text")

    def _opencode_models(self):
        """Zen model ids to try, in order: OPENCODE_MODELS env wins."""
        return self._env_models("OPENCODE_MODELS", ZEN_DEFAULT_MODELS)

    @staticmethod
    def _env_models(env_name: str, defaults):
        """Model roster from an env var (comma-separated), else defaults."""
        configured = os.environ.get(env_name, "")
        models = [m.strip() for m in configured.split(",") if m.strip()]
        return models or list(defaults)

    def _try_openai_compatible(self, label, base_url, api_key, models, prompt,
                               extra_headers=None):
        """Shared runner for OpenAI-compatible chat providers.

        Returns the report text from the first model that answers with
        non-empty content; per-model failures are logged and the chain
        falls through. No key -> None without any HTTP call.
        """
        if not api_key:
            return None
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        if extra_headers:
            headers.update(extra_headers)
        for model_name in models:
            try:
                response = requests.post(
                    f"{base_url}/chat/completions",
                    headers=headers,
                    json={
                        "model": model_name,
                        "messages": [{"role": "user", "content": prompt}],
                    },
                    timeout=180,
                )
                if response.status_code != 200:
                    snippet = response.text[:200].replace("\n", " ")
                    print(
                        f"{label} attempt failed with model {model_name}: "
                        f"HTTP {response.status_code} {snippet}"
                    )
                    continue
                payload = response.json()
                content = (
                    payload.get("choices", [{}])[0]
                    .get("message", {})
                    .get("content")
                )
                if content and content.strip():
                    print(f"{label} report generated with model: {model_name}")
                    return content
                print(f"{label} returned empty content for model {model_name}")
            except Exception as error:
                print(f"{label} attempt failed with model {model_name}: {error}")
        return None

    def _try_openrouter_chain(self, prompt: str):
        """Fallback #1: OpenRouter free models (full prompt).

        Free tier is capped by requests (20/min, 50/day), not tokens,
        and contexts run 128K-1M, so the full briefing prompt fits.
        The free lineup rotates; OPENROUTER_MODELS overrides the roster.
        """
        return self._try_openai_compatible(
            "OpenRouter",
            os.environ.get("OPENROUTER_BASE_URL", OPENROUTER_BASE_URL).rstrip("/"),
            os.environ.get("OPENROUTER_" "API_KEY"),
            self._env_models("OPENROUTER_MODELS", OPENROUTER_DEFAULT_MODELS),
            prompt,
            extra_headers={"X-Title": "breaksNew IT Briefing"},
        )

    def _try_groq_chain(self, prompt: str):
        """Fallback #2: Groq free tier (COMPACT prompt — see caller).

        Groq's free tier is permanent and card-free, but large models
        are capped at 8-12K tokens/minute, so this chain is only ever
        called with the trimmed payload.
        """
        return self._try_openai_compatible(
            "Groq",
            os.environ.get("GROQ_BASE_URL", GROQ_BASE_URL).rstrip("/"),
            os.environ.get("GROQ_" "API_KEY"),
            self._env_models("GROQ_MODELS", GROQ_DEFAULT_MODELS),
            prompt,
        )

    def _try_opencode_chain(self, prompt: str):
        """Fallback #3: OpenCode Zen, if a key/token is set.

        Note: Zen's free (*-free) models have been gated to the OpenCode
        app since 2026-09 — external calls from datacenter IPs get
        HTTP 429 FreeUsageLimitError (verified live 2026-11-01), so this
        chain is a best-effort last resort; it still works with paid
        Zen ids or an OpenCode Go key, where external access is allowed.
        """
        return self._try_openai_compatible(
            "OpenCode Zen",
            os.environ.get("OPENCODE_BASE_URL", ZEN_BASE_URL).rstrip("/"),
            os.environ.get("OPENCODE_" "API_KEY"),
            self._opencode_models(),
            prompt,
        )

    def _try_model(self, model_name: str, prompt: str):
        """Try one model via generateContent, then via the Interactions API.

        Newer models (3.8 family) are served through Google's Interactions
        API; generateContent may refuse them, so both surfaces are tried
        before giving up on the model.
        """
        try:
            response = self.client.models.generate_content(
                model=model_name,
                contents=prompt,
            )
            if response and getattr(response, "text", None):
                return response.text
        except Exception as error:
            print(f"Gemini API attempt failed with model {model_name}: {error}")

        interactions = getattr(self.client, "interactions", None)
        if interactions is not None:
            try:
                interaction = interactions.create(model=model_name, input=prompt)
                text = self._extract_interaction_text(interaction)
                if text:
                    return text
            except Exception as error:
                print(f"Gemini Interactions attempt failed with model {model_name}: {error}")
        return None

    @staticmethod
    def _extract_interaction_text(interaction) -> str | None:
        """Best-effort text extraction from an Interactions API response."""
        if interaction is None:
            return None
        output_text = getattr(interaction, "output_text", None)
        if isinstance(output_text, str) and output_text.strip():
            return output_text
        for container_name in ("outputs", "output"):
            container = getattr(interaction, container_name, None)
            if isinstance(container, str) and container.strip():
                return container
            if isinstance(container, (list, tuple)):
                parts = []
                for entry in container:
                    if isinstance(entry, str):
                        parts.append(entry)
                        continue
                    entry_text = getattr(entry, "text", None)
                    if isinstance(entry_text, str):
                        parts.append(entry_text)
                        continue
                    content = getattr(entry, "content", None)
                    if isinstance(content, (list, tuple)):
                        for part in content:
                            part_text = getattr(part, "text", None)
                            if isinstance(part_text, str):
                                parts.append(part_text)
                joined = "".join(parts).strip()
                if joined:
                    return joined
        return None

    def _top_insight_comments(self, items: List[RawItem], limit: int = 5):
        """Best directional comments across all items: (item, comment, insight)."""
        pool = []
        for item in items:
            for comment in item.top_comments:
                pool.append((item, comment, comment_insight_score(comment.text)))
        pool.sort(key=lambda entry: (entry[2], entry[1].votes), reverse=True)
        return pool[:limit]

    def _build_fallback_report(self, items: List[RawItem]) -> str:
        """Structured listing of the *filtered* items, direction-first.

        Leads with the best directional community comments (full text, up
        to the normalizer's 700-char cap) — for this briefing those
        comments ARE the product — then the ranked source list.
        """
        ranked = self._ranked(items)
        lines = [
            "# BÁO CÁO ĐỊNH HƯỚNG NGÀNH IT (BẢN LỌC TỰ ĐỘNG)",
            "",
        ]
        if not ranked:
            lines.append("Hôm nay không có nguồn nào đạt ngưỡng liên quan tối thiểu.")
            return "\n".join(lines)

        lines.append("## BÌNH LUẬN ĐỊNH HƯỚNG NỔI BẬT")
        lines.append("")
        top_comments = self._top_insight_comments(ranked)
        if top_comments:
            for item, comment, insight in top_comments:
                votes_label = f"{comment.votes} votes" if comment.votes else "HN comment"
                lines.append(
                    f"### Từ [{item.title}]({item.url}) ({item.source_name})"
                )
                lines.append(f"*{comment.author}* ({votes_label}, insight {insight:.0f}):")
                lines.append(f"> {comment.text}")
                lines.append("")
        else:
            lines.append("Chưa thu được bình luận cộng đồng nào trong lần chạy này.")
            lines.append("")

        incidents = [i for i in ranked if is_major_incident(i)][:INCIDENT_PROMPT_MAX]
        if incidents:
            lines.append("## SỰ CỐ CÔNG NGHỆ LỚN HÔM NAY")
            lines.append("")
            for item in incidents:
                lines.append(f"### [{item.title}]({item.url}) ({item.source_name})")
                lines.append(
                    f"**Mức nghiêm trọng (severity):** "
                    f"{incident_severity_score(item):.0f} · {item.score_reason}"
                )
                if item.summary_text:
                    lines.append(f"**Tóm tắt nội dung:** {item.summary_text[:280]}...")
                lines.append("")

        lines.append("## NGUỒN ĐÃ LỌC THEO ĐIỂM LIÊN QUAN")
        lines.append("")
        for item in ranked[:15]:
            topics = ", ".join(item.matched_topics) if item.matched_topics else "—"
            lines.append(
                f"### [{item.title}]({item.url}) ({item.source_name})"
            )
            lines.append(
                f"**Điểm liên quan:** {item.relevance_score:.0f} · "
                f"**Chủ đề:** {topics} · **Vì sao chọn:** {item.score_reason}"
            )
            if item.summary_text:
                lines.append(f"**Tóm tắt nội dung:** {item.summary_text[:280]}...")
                if item.region == "GLOBAL":
                    lines.append(f"> English reference: {item.summary_text[:180]}...")
            if item.top_comments:
                lines.append("**Bình luận nổi bật từ cộng đồng:**")
                for c in rank_comments(item.top_comments, limit=3):
                    votes_label = f"{c.votes} votes" if c.votes else "HN comment"
                    lines.append(f"- *{c.author}* ({votes_label}): \"{c.text}\"")
            lines.append("")
        return "\n".join(lines)
