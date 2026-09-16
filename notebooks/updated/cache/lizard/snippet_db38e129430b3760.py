def _unique_class(self, cls):
    return not any(isinstance(obj, cls) for obj in self.plugins)