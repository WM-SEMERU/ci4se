def itermerged(self):
    for key in self:
        val = _dict_getitem(self, key)
        yield val[0], ', '.join(val[1:])