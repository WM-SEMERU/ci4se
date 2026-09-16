def load_ctypes_library(name):
    try:
        return cdll.LoadLibrary(name)
    except OSError:
        name = find_library(name)
        if name is None:
            raise
        return cdll.LoadLibrary(name)