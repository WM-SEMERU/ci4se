def setTableType(self, tableType):
    self.navigator().setTableType(tableType)
    completer = XJoinCompleter(self.navigator().model(), self)
    completer.setCompletionMode(XJoinCompleter.InlineCompletion)
    self.setCompleter(completer)