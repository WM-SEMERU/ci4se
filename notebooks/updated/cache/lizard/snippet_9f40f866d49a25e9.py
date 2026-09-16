def setText(self, text):
    self._text = nativestring(text)
    if self.showRichText():
        self.richTextLabel().setText(text)
    else:
        super(XPushButton, self).setText(text)