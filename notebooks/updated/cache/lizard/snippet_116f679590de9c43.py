def add_name_variant(self, name):
    self._ensure_field('name', {})
    self.obj['name'].setdefault('name_variants', []).append(name)