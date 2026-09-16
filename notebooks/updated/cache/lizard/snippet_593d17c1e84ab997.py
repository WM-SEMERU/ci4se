def remove_all_matching(self, address=None, name=None):
    if self.entries:
        if address and name:
            func = lambda entry: not entry.is_real_entry(
                ) or entry.address != address and name not in entry.names
        elif address:
            func = lambda entry: not entry.is_real_entry(
                ) or entry.address != address
        elif name:
            func = lambda entry: not entry.is_real_entry(
                ) or name not in entry.names
        else:
            raise ValueError('No address or name was specified for removal.')
        self.entries = list(filter(func, self.entries))