def add_field(self, field, **kwargs):
    getattr(self, self._private_fields_name).append(field)
    self._expire_cache(reverse=True)
    self._expire_cache(reverse=False)