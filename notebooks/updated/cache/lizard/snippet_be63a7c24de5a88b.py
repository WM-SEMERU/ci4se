def iscallable(self, objtxt):
    obj, valid = self._eval(objtxt)
    if valid:
        return callable(obj)