def get_introspection_module(namespace):
    if namespace in _introspection_modules:
        return _introspection_modules[namespace]
    from . import get_required_version
    repository = GIRepository()
    version = get_required_version(namespace)
    try:
        repository.require(namespace, version, 0)
    except GIError as e:
        raise ImportError(e.message)
    library = repository.get_shared_library(namespace)
    if library:
        library = library.split(',')[0]
        try:
            util.load_ctypes_library(library)
        except OSError:
            raise ImportError("Couldn't load shared library %r" % library)
    instance = Module(repository, namespace)
    instance.__path__ = repository.get_typelib_path(namespace)
    instance.__package__ = const.PREFIX[0]
    instance.__file__ = '<%s.%s>' % (const.PREFIX[0], namespace)
    instance._version = version or repository.get_version(namespace)
    _introspection_modules[namespace] = instance
    return instance