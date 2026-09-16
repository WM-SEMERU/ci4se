def described_as(self, description, *args):
    if len(args):
        description = description.format(*args)
    self.description = description
    return self