def _make_kind_id(self, name_or_id):
    if not name_or_id:
        return None
    if name_or_id.isdigit():
        return name_or_id
    return self.kind_name_to_id(name_or_id)