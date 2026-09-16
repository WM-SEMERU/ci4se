def setError(self, msg=None, title=None):
    if msg is not None:
        self.messageLabel.setText(msg)
    if title is not None:
        self.titleLabel.setText(title)