// Webhook receiver for the IT Market Briefing pipeline.
//
// Two paths:
//  1. Document tabs via the advanced Docs service: text is inserted raw
//     (Apps Script cannot restyle a tab body afterwards). For fully
//     formatted tabs, prefer the Python service-account path in
//     src/publishers/google_docs_publisher.py, which converts markdown to
//     real Docs headings/bullets/links.
//  2. Fallback (no tabs): the markdown is PARSED line-by-line and appended
//     as real headings, bullets, quotes and paragraphs with bold/link
//     styling — never as one giant raw paragraph like before.

function parseInline_(text) {
  var plain = "";
  var spans = [];
  var re = /(\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\)|\*[^*]+\*|`[^`]+`)/g;
  var last = 0;
  var m;
  while ((m = re.exec(text)) !== null) {
    plain += text.slice(last, m.index);
    var token = m[0];
    var start = plain.length;
    if (token.indexOf("**") === 0) {
      var innerBold = token.slice(2, -2);
      plain += innerBold;
      spans.push({ start: start, length: innerBold.length, bold: true });
    } else if (token.charAt(0) === "[") {
      var linkMatch = token.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
      plain += linkMatch[1];
      spans.push({ start: start, length: linkMatch[1].length, linkUrl: linkMatch[2] });
    } else if (token.charAt(0) === "`") {
      plain += token.slice(1, -1);
    } else {
      var innerItalic = token.slice(1, -1);
      plain += innerItalic;
      spans.push({ start: start, length: innerItalic.length, italic: true });
    }
    last = m.index + token.length;
  }
  plain += text.slice(last);
  return { plain: plain, spans: spans };
}

function applyInline_(element, parsed) {
  try {
    var txt = element.editAsText();
    txt.setText(parsed.plain);
    parsed.spans.forEach(function (span) {
      var end = span.start + span.length - 1;
      if (span.length <= 0) return;
      if (span.bold) txt.setBold(span.start, end, true);
      if (span.italic) txt.setItalic(span.start, end, true);
      if (span.linkUrl) txt.setLinkUrl(span.start, end, span.linkUrl);
    });
  } catch (err) {
    try { element.setText(parsed.plain); } catch (ignored) {}
  }
}

function appendMarkdown_(body, content) {
  var lines = (content || "").split("\n");
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i].replace(/\s+$/, "");
    if (!line.trim()) continue;
    if (/^(\*\*\*|---|___)\s*$/.test(line.trim())) continue;

    var heading = line.match(/^(#{1,6})\s+(.*)$/);
    var quote = line.match(/^>\s?(.*)$/);
    var bullet = line.match(/^[-*+]\s+(.*)$/) || line.match(/^\d+[.)]\s+(.*)$/);

    if (heading) {
      var levels = [
        DocumentApp.ParagraphHeading.TITLE,
        DocumentApp.ParagraphHeading.HEADING1,
        DocumentApp.ParagraphHeading.HEADING2,
        DocumentApp.ParagraphHeading.HEADING3,
        DocumentApp.ParagraphHeading.HEADING4,
        DocumentApp.ParagraphHeading.HEADING5
      ];
      var p = body.appendParagraph("");
      p.setHeading(levels[heading[1].length - 1]);
      applyInline_(p, parseInline_(heading[2]));
    } else if (quote) {
      var q = body.appendParagraph("");
      var parsedQuote = parseInline_(quote[1]);
      parsedQuote.spans.push({ start: 0, length: parsedQuote.plain.length, italic: true });
      applyInline_(q, parsedQuote);
    } else if (bullet) {
      var item = body.appendListItem("");
      item.setGlyphType(DocumentApp.GlyphType.BULLET);
      applyInline_(item, parseInline_(bullet[1]));
    } else {
      var para = body.appendParagraph("");
      applyInline_(para, parseInline_(line.trim()));
    }
  }
}

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var dateStr = data.date || Utilities.formatDate(new Date(), "GMT+7", "yyyy-MM-dd");
    var content = data.content || "";
    var doc = DocumentApp.getActiveDocument();
    var docId = doc.getId();

    var tabId = "";
    try {
      if (typeof Docs !== "undefined") {
        var createTabResponse = Docs.Documents.batchUpdate({
          requests: [{
            addDocumentTab: {
              tabProperties: {
                title: dateStr
              }
            }
          }]
        }, docId);
        tabId = createTabResponse.replies[0].addDocumentTab.tabProperties.tabId;
        Docs.Documents.batchUpdate({
          requests: [{
            insertText: {
              location: { tabId: tabId, index: 1 },
              text: content
            }
          }]
        }, docId);
      }
    } catch (tabError) {
      tabId = "";
    }

    if (!tabId) {
      var body = doc.getBody();
      if (body.getText().length > 0) {
        body.appendPageBreak();
      }
      var titleParagraph = body.appendParagraph("BÁO CÁO THỊ TRƯỜNG IT - " + dateStr);
      titleParagraph.setHeading(DocumentApp.ParagraphHeading.HEADING1);
      appendMarkdown_(body, content);
      doc.saveAndClose();
    }

    var docUrl = tabId ? "https://docs.google.com/document/d/" + docId + "/edit?tab=" + tabId : doc.getUrl();

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      url: docUrl
    })).setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
