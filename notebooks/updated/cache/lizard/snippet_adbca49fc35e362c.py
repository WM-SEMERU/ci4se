def set_not_found_handler(self, handler, version=None):
    if not self.not_found_handlers:
        self._not_found_handlers = {}
    self.not_found_handlers[version] = handler