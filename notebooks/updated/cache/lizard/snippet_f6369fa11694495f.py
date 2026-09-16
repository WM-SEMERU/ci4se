def handleError(self, test, err):
    want_error = self._handle_test_error_or_failure(test, err)
    if not want_error and id(test) in self._tests_that_reran:
        self._nose_result.addError(test, err)
    return want_error or None