def set_result(self, result):
    if self.is_finished():
        raise InternalError(
            'set_result called on finished AsynchronousResponse', result=
            self._result, exception=self._exception)
    self._result = result
    self.finish()