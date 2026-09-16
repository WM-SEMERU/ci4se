def set_option(self, key, value):
    self._options.update(self._option_schema({key: value}))
    self.clear_cache()