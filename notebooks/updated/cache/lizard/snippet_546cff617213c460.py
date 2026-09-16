def _deleter(self, obj):
    if self._fdel_ is not None:
        self._fdel_(obj)
    else:
        delattr(obj, self._attrname())
    if isinstance(obj, Schema):
        obj._delvalue(self)