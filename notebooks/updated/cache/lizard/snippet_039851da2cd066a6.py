def bank_name(self):
    entry = registry.get('bic').get(self.compact)
    if entry:
        return entry.get('name')