def isValue(self):
    if self._currentIdx is None:
        return False
    componentValue = self._componentValues[self._currentIdx]
    return componentValue is not noValue and componentValue.isValue