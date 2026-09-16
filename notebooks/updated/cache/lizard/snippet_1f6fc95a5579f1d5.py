def set_recording(is_recording):
    prev = ctypes.c_int()
    check_call(_LIB.MXAutogradSetIsRecording(ctypes.c_int(is_recording),
        ctypes.byref(prev)))
    return bool(prev.value)