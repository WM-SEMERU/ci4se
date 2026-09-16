def to_dict(self, flat=True):
    if flat:
        return dict(self.items())
    return dict(self.lists())