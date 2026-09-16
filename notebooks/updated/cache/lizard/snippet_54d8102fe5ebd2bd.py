def only(self, *fields):
    clone = self._clone()
    clone._fields = fields
    return clone