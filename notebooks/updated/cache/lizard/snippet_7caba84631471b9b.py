def load(self, name, parent_path=None):
    if name not in self.templates:
        self.templates[name] = self._create_template(name)
    return self.templates[name]