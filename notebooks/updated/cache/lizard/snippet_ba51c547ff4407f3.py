def _makeExtraWidgets(self):
    self.textWidget = urwid.Text(self.text)
    return [self.textWidget]