def currentContentsWidget(self, autoadd=False):
    widget = self.uiContentsTAB.widget(self.currentContentsIndex())
    if not isinstance(widget, QWebView):
        widget = None
    if not widget and autoadd:
        widget = self.addContentsWidget()
    return widget