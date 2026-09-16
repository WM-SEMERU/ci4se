def scan_for_field(self, field_key):
    if field_key == self.get_name():
        return self
    if field_key in self._fields_dict:
        return self._fields_dict[field_key]
    for field in self._fields:
        if isinstance(field, Container):
            resolved = field.scan_for_field(field_key)
            if resolved:
                return resolved
    return None