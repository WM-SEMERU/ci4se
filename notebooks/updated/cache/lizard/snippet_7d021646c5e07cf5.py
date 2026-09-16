def modify(self, entry_id, **kw):
    entry = self.read(entry_id)
    for k, v in kw.items():
        setattr(entry, k, v)
    self.update(entry)
    return True