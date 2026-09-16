def filter_metadata(self, key):
    filtered = [field[key] for field in self.metadata if key in field]
    if len(filtered) == 0:
        raise KeyError('Key not found in metadata')
    return filtered