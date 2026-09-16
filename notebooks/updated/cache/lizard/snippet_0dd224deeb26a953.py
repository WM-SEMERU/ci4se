def _deserialize(self, value, attr, data, partial=None, **kwargs):
    self._test_collection(value)
    return self._load(value, data, partial=partial)