def create(self, **fields):
    entry = self.instance(**fields)
    entry.save()
    return entry