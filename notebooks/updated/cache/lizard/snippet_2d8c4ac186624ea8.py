def set_linetrace_on_frame(f, localtrace=None):
    traceptr, _, _ = get_frame_pointers(f)
    if localtrace is not None:
        ctypes.pythonapi.Py_IncRef(localtrace)
        addr = id(localtrace)
    else:
        addr = 0
    traceptr.contents = ctypes.py_object.from_address(addr)