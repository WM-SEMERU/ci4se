def base_fields(self):
    if self.extensions_start is None:
        return len(self.fields)
    return len(self.fields[:self.extensions_start])