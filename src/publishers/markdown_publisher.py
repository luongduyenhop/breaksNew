import os
from datetime import datetime

class MarkdownPublisher:
    def __init__(self, output_dir: str = "reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def publish(self, content: str, date_str: str = None) -> str:
        date_tag = date_str or datetime.now().strftime("%Y-%m-%d")
        file_path = os.path.join(self.output_dir, f"IT_Briefing_{date_tag}.md")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        return file_path
