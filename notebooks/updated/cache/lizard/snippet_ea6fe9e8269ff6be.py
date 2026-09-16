def getElementDeclaration(cls, namespaceURI, name, isref=False, lazy=False):
    key = namespaceURI, name
    if isref:
        klass = cls.elements.get(key, None)
        if klass is not None and lazy is True:
            return _Mirage(klass)
        return klass
    typecode = cls.element_typecode_cache.get(key, None)
    if typecode is None:
        tcls = cls.elements.get(key, None)
        if tcls is not None:
            typecode = cls.element_typecode_cache[key] = tcls()
            typecode.typed = False
    return typecode