def add_result_handler(self, handler):
    self._result_handlers.append(handler)
    if self._sorted_handlers:
        self._sorted_handlers = None