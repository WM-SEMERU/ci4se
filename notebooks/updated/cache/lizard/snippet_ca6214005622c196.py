def flatten_dict(self, obj):
    return OrderedDict(zip(self.fieldnames, self.flatten(obj)))