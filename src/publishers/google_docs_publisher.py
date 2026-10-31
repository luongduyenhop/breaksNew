import os
import json
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build

class GoogleDocsPublisher:
    def __init__(self):
        self.webhook_url = os.environ.get("GOOGLE_DOCS_WEBHOOK_URL")
        self.doc_id = os.environ.get("GOOGLE_DOC_ID")
        self.sa_env = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
        self.scopes = [
            "https://www.googleapis.com/auth/documents",
            "https://www.googleapis.com/auth/drive"
        ]
        self.credentials = None
        if self.sa_env:
            try:
                info = json.loads(self.sa_env)
                self.credentials = service_account.Credentials.from_service_account_info(
                    info, scopes=self.scopes
                )
            except Exception:
                self.credentials = None

    def publish_document(self, tab_title: str, markdown_content: str) -> str:
        if self.webhook_url:
            return self._publish_via_webhook(tab_title, markdown_content)
        if self.credentials:
            return self._publish_via_api(tab_title, markdown_content)
        print("Google Docs skipped: neither GOOGLE_DOCS_WEBHOOK_URL nor GOOGLE_SERVICE_ACCOUNT_JSON is set in .env")
        return ""

    def _publish_via_webhook(self, tab_title: str, markdown_content: str) -> str:
        try:
            payload = {
                "date": tab_title,
                "content": markdown_content
            }
            response = requests.post(self.webhook_url, json=payload, timeout=35, allow_redirects=True)
            if response.status_code == 200:
                result = response.json()
                if result.get("status") == "success":
                    return result.get("url", "")
                print(f"Google Docs Webhook message: {result.get('message')}")
            else:
                print(f"Google Docs Webhook HTTP status: {response.status_code}")
        except Exception as error:
            print(f"Google Docs Webhook request failed: {error}")
        return ""

    def _publish_via_api(self, tab_title: str, markdown_content: str) -> str:
        try:
            docs_service = build("docs", "v1", credentials=self.credentials)
            drive_service = build("drive", "v3", credentials=self.credentials)

            target_doc_id = self.doc_id
            if not target_doc_id:
                new_doc = docs_service.documents().create(body={"title": "IT Market Briefings (Daily Tabs)"}).execute()
                target_doc_id = new_doc.get("documentId")
                drive_service.permissions().create(
                    fileId=target_doc_id,
                    body={"type": "anyone", "role": "reader"}
                ).execute()

            try:
                add_tab_response = docs_service.documents().batchUpdate(
                    documentId=target_doc_id,
                    body={
                        "requests": [
                            {
                                "addDocumentTab": {
                                    "tabProperties": {
                                        "title": tab_title
                                    }
                                }
                            }
                        ]
                    }
                ).execute()

                tab_id = add_tab_response["replies"][0]["addDocumentTab"]["tabProperties"]["tabId"]

                docs_service.documents().batchUpdate(
                    documentId=target_doc_id,
                    body={
                        "requests": [
                            {
                                "insertText": {
                                    "location": {
                                        "tabId": tab_id,
                                        "index": 1
                                    },
                                    "text": markdown_content
                                }
                            }
                        ]
                    }
                ).execute()

                return f"https://docs.google.com/document/d/{target_doc_id}/edit?tab={tab_id}"
            except Exception:
                docs_service.documents().batchUpdate(
                    documentId=target_doc_id,
                    body={
                        "requests": [
                            {
                                "insertText": {
                                    "location": {
                                        "index": 1
                                    },
                                    "text": f"\n\n# {tab_title}\n\n{markdown_content}\n"
                                }
                            }
                        ]
                    }
                ).execute()
                return f"https://docs.google.com/document/d/{target_doc_id}/edit"
        except Exception as error:
            print(f"Google Docs API failed: {error}")
            return ""
