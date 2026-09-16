def _clone(self):
    cls = self.__class__
    q = cls.__new__(cls)
    q.__dict__ = self.__dict__.copy()
    q._params = self._params.copy()
    q._headers = self._headers.copy()
    q._attribute_stack = self._attribute_stack[:]
    return q