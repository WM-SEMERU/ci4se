def handleFailure(self, test, err):
    want_failure = self._handle_test_error_or_failure(test, err)
    if not want_failure and id(test) in self._tests_that_reran:
        self._nose_result.addFailure(test, err)
    return want_failure or None