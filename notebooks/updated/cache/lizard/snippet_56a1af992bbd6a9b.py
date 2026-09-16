def currentAction(self):
    if not self._actionGroup:
        return None
    for act in self._actionGroup.actions():
        if act.isChecked():
            return act
    return None