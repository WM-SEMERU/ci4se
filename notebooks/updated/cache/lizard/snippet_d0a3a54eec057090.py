def set_as_underlined(self, color=Qt.blue):
    self.format.setUnderlineStyle(QTextCharFormat.SingleUnderline)
    self.format.setUnderlineColor(color)