def fill_into_dict(self, items, dest):
    for item in items:
        dest[self.key(item)].append(item)