def _updateTargetFromNode(self):
    if self.axisNumber == X_AXIS:
        xMode, yMode = self.configValue, None
    else:
        xMode, yMode = None, self.configValue
    self.plotItem.setLogMode(x=xMode, y=yMode)