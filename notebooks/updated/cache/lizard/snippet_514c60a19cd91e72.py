def set_colors(self, text='black', background='white'):
    if self._multiline:
        self._widget.setStyleSheet('QTextEdit {background-color: ' + str(
            background) + '; color: ' + str(text) + '}')
    else:
        self._widget.setStyleSheet('QLineEdit {background-color: ' + str(
            background) + '; color: ' + str(text) + '}')