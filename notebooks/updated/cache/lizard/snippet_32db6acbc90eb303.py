def addUnexpectedSuccess(self, test):
    result = self._handle_result(test, TestCompletionStatus.unexpected_success)
    self.unexpectedSuccesses.append(result)