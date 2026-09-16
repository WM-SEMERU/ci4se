def findAction(self, text):
    for action in self.actionGroup().actions():
        if text in (action.objectName(), action.text()):
            return action
    return None