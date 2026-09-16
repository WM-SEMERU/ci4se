def _ph2f(self, placeholder):
    if issubclass(placeholder.cls, FieldAccessor):
        return placeholder.cls.access(self._parent, placeholder)
    return self._parent.lookup_field_by_placeholder(placeholder)