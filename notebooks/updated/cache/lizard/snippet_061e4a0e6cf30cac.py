def freeze(self):
    if self.value is None:
        self.value = ''
    if self.dialect in [DIALECT_ALTREE]:
        name_tuple = parse_name_altree(self)
    elif self.dialect in [DIALECT_MYHERITAGE]:
        name_tuple = parse_name_myher(self)
    elif self.dialect in [DIALECT_ANCESTRIS]:
        name_tuple = parse_name_ancestris(self)
    else:
        name_tuple = split_name(self.value)
    self.value = name_tuple
    return self