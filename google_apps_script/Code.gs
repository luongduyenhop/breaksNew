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
      body.appendParagraph(content);
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
