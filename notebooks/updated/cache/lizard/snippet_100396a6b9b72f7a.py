def copy(self, keep_fields=None):
    keep_fields = self.fields.keys() or keep_fields
    return self.__class__(OrderedDict([(name, data[:]) for name, data in
        self.fields.items() if name in keep_fields]))