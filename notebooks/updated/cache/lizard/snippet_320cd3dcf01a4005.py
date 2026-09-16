def add(self, *value):
    flattenedValueList = list(flatten(value))
    return self._add(flattenedValueList, self.value)