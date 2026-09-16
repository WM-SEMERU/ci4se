def spy(object):
    if inspect.isclass(object) or inspect.ismodule(object):
        class_ = None
    else:
        class_ = object.__class__


    class Spy(_Dummy):
        if class_:
            __class__ = class_

        def __getattr__(self, method_name):
            return RememberedProxyInvocation(theMock, method_name)

        def __repr__(self):
            name = 'Spied'
            if class_:
                name += class_.__name__
            return '<%s id=%s>' % (name, id(self))
    obj = Spy()
    theMock = Mock(obj, strict=True, spec=object)
    mock_registry.register(obj, theMock)
    return obj