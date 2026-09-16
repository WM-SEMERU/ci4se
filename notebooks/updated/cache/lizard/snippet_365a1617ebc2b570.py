def toggleActions(self, value=True):
    for z in self.actions.zoomActions:
        z.setEnabled(value)
    for action in self.actions.onLoadActive:
        action.setEnabled(value)