def set_result(self, result):
    self._result = result
    self._result_set = True
    self._invoke_callbacks(self)