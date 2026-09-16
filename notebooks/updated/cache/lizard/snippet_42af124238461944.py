def to_dict(self, flat=True):
    if flat:
        return dict(self.iteritems())
    return dict(self.lists())