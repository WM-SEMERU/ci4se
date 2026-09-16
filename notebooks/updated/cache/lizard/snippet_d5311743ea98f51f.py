def _get_child_mock(self, **kw):
    _type = type(self)
    if not issubclass(_type, CallableMixin):
        if issubclass(_type, NonCallableMagicMock):
            klass = MagicMock
        elif issubclass(_type, NonCallableMock):
            klass = Mock
    else:
        klass = _type.__mro__[1]
    return klass(**kw)