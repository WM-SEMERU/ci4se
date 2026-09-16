def load(self, **kwargs):
    self._is_version_supported_method('12.1.0')
    newinst = self._stamp_out_core()
    newinst._refresh(**kwargs)
    return newinst