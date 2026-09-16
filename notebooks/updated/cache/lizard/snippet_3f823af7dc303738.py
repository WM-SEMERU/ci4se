def add_entry(self, entry):
    self.entry_keys.setdefault(entry, [])
    self.entries.append(entry)
    for dist in find_distributions(entry, True):
        self.add(dist, entry, False)