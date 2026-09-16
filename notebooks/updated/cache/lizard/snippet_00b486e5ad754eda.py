def get(self, name, template_path):
    if name not in self._renderers:
        cls = self._renderer_classes.get(name)
        if cls is None:
            return None
        else:
            self._renderers[name] = cls(template_path, self.extra_vars)
    return self._renderers[name]