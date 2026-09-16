def import_deleted_fields(self, data):
    if self.get_read_only() and self.is_locked():
        return
    if isinstance(data, str):
        data = [data]
    for key in data:
        if hasattr(self, key):
            delattr(self, key)
            continue
        keys = key.split('.', 1)
        if len(keys) != 2:
            continue
        child = getattr(self, keys[0])
        child.import_deleted_fields(keys[1])