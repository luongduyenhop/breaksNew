import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown

class GmailPublisher:
    def __init__(self):
        self.sender_email = os.environ.get("GMAIL_USER", "").strip()
        raw_password = os.environ.get("GMAIL_APP_PASSWORD", "")
        self.app_password = raw_password.replace(" ", "").strip()
        self.recipient_email = os.environ.get("RECIPIENT_EMAIL", "").strip() or self.sender_email

    def send_briefing_email(self, subject: str, markdown_content: str, google_docs_url: str = "") -> bool:
        if not self.sender_email or "your_email" in self.sender_email:
            print("Email skipped: GMAIL_USER is still set to placeholder in .env. Please replace with your actual Gmail address.")
            return False
        if not self.app_password or "your_16" in self.app_password:
            print("Email skipped: GMAIL_APP_PASSWORD is still set to placeholder in .env.")
            return False
        if not self.recipient_email or "your_email" in self.recipient_email:
            print("Email skipped: RECIPIENT_EMAIL is still set to placeholder in .env.")
            return False

        html_body = markdown.markdown(markdown_content, extensions=["extra", "tables"])
        banner_html = ""
        if google_docs_url:
            banner_html = f"""
            <div style="background-color: #e8f0fe; border-left: 5px solid #1a73e8; padding: 16px 20px; margin-bottom: 24px; border-radius: 6px;">
                <p style="margin: 0; font-size: 16px; color: #1a73e8; font-weight: bold;">
                    📑 Bản Google Docs trực tuyến (Tab mới hôm nay):
                </p>
                <p style="margin: 8px 0 0 0;">
                    <a href="{google_docs_url}" target="_blank" style="display: inline-block; background-color: #1a73e8; color: #ffffff; text-decoration: none; padding: 8px 16px; border-radius: 4px; font-weight: 500; font-size: 14px;">
                        Mở Google Docs tab hôm nay &rarr;
                    </a>
                </p>
            </div>
            """

        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                    line-height: 1.65;
                    color: #202124;
                    max-width: 820px;
                    margin: 0 auto;
                    padding: 24px;
                }}
                h1 {{ color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 8px; font-size: 24px; }}
                h2 {{ color: #174ea6; margin-top: 24px; font-size: 20px; }}
                h3 {{ color: #3c4043; font-size: 16px; }}
                blockquote {{
                    background-color: #f8f9fa;
                    border-left: 4px solid #bdc1c6;
                    margin: 12px 0;
                    padding: 8px 16px;
                    color: #5f6368;
                    font-style: italic;
                }}
                code {{
                    background-color: #f1f3f4;
                    padding: 2px 6px;
                    border-radius: 4px;
                    font-size: 90%;
                }}
                a {{ color: #1a73e8; text-decoration: none; }}
                a:hover {{ text-decoration: underline; }}
                ul, ol {{ padding-left: 24px; }}
                li {{ margin-bottom: 6px; }}
            </style>
        </head>
        <body>
            {banner_html}
            {html_body}
        </body>
        </html>
        """

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"IT Market Briefing <{self.sender_email}>"
        msg["To"] = self.recipient_email

        msg.attach(MIMEText(markdown_content, "plain", "utf-8"))
        msg.attach(MIMEText(full_html, "html", "utf-8"))

        try:
            with smtplib.SMTP("smtp.gmail.com", 587, timeout=25) as server:
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(self.sender_email, self.app_password)
                server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
            return True
        except Exception as error_587:
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=25) as server:
                    server.login(self.sender_email, self.app_password)
                    server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
                return True
            except Exception as error_465:
                print(f"Gmail sending failed: Port 587 ({error_587}) | Port 465 ({error_465})")
                return False
