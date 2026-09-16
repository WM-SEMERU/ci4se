def cxx(source, libraries=[]):
    r
    path = _cc_build_shared_lib(source, '.cc', libraries)
    return ctypes.cdll.LoadLibrary(path)