def clear(self):
    super(XTextEdit, self).clear()
    self.textEntered.emit('')
    self.htmlEntered.emit('')
    if self.autoResizeToContents():
        self.resizeToContents()