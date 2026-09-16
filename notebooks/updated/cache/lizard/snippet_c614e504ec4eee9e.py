def _nodeGetNonDefaultsDict(self):
    dct = {}
    if self.data != self.defaultData:
        dct['data'] = self.data.name()
    return dct