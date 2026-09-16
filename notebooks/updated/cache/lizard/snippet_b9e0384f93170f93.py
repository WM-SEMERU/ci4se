def setCurrentInspectorRegItem(self, regItem):
    check_class(regItem, InspectorRegItem, allow_none=True)
    self.inspectorTab.setCurrentRegItem(regItem)