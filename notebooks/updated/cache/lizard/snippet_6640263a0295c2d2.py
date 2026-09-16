def get_processor_name():
    mxlen = 256
    length = ctypes.c_ulong()
    buf = ctypes.create_string_buffer(mxlen)
    _LIB.RabitGetProcessorName(buf, ctypes.byref(length), mxlen)
    return buf.value