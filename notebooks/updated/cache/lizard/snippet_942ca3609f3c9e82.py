def init_backends():
    global _BACKENDS, _ACTIVE_BACKENDS
    try:
        from .cffi_backend import CFFIBackend
    except ImportError:
        pass
    else:
        _BACKENDS.append(CFFIBackend)
    from .ctypes_backend import CTypesBackend
    from .null_backend import NullBackend
    _BACKENDS.append(CTypesBackend)
    _ACTIVE_BACKENDS = _BACKENDS[:]
    _BACKENDS.append(NullBackend)