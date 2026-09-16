def Expand(self, obj, path):
    if isinstance(path, py2to3.STRING_TYPES):
        path = path.split(self.FIELD_SEPARATOR)
    attr_name = self._GetAttributeName(path)
    attr_value = self._GetValue(obj, attr_name)
    if attr_value is None:
        return
    if len(path) == 1:
        for value in self._AtLeaf(attr_value):
            yield value
    else:
        for value in self._AtNonLeaf(attr_value, path):
            yield value