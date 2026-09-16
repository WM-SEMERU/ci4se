def setMaximumSize(self, *args):
    super(XView, self).setMaximumSize(*args)
    if not self.signalsBlocked():
        self.sizeConstraintChanged.emit()