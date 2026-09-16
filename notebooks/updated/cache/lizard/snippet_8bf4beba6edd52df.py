def get_extensions(self, klass):
    self.discover_extensions()
    return self._extensions.get(self._get_class_path(klass), [])