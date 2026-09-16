def validate(self):
    for name, field in self._fields.items():
        v = getattr(self, name)
        if v is None and not self._values[name].explicit and field.has_default:
            v = field.get_default()
        val = field.validate(v)
        setattr(self, name, val)