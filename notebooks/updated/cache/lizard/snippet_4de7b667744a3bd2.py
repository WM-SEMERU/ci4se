def throw(self, typ, val=None, tb=None):
    if self._hub is None or not self._fiber.is_alive():
        return
    self._hub.run_callback(self._fiber.throw, typ, val, tb)
    self._hub = self._fiber = None