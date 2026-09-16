def go_to(self, url_or_text):
    if is_text_string(url_or_text):
        url = QUrl(url_or_text)
    else:
        url = url_or_text
    self.webview.load(url)