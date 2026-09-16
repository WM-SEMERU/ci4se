def setWebView(self, webView):
    if self._webView:
        self._webView.removeAction(self._findAction)
    self._webView = webView
    if webView:
        webView.addAction(self._findAction)