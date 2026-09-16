def _get_request_fields_from_parent(self):
    if not self.parent:
        return None
    if not getattr(self.parent, 'request_fields'):
        return None
    if not isinstance(self.parent.request_fields, dict):
        return None
    return self.parent.request_fields.get(self.field_name)