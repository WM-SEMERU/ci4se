def _remap(object, name, value, safe=True):
    if os.getenv('QT_TESTING') is not None and safe:
        if hasattr(object, name):
            raise AttributeError('Cannot override existing name: %s.%s' % (
                object.__name__, name))
        if type(object).__name__ != 'module':
            raise AttributeError(
                "%s != 'module': Cannot alter anything but modules" % object)
    elif hasattr(object, name):
        self.__modified__.append(name)
    self.__remapped__.append(name)
    setattr(object, name, value)