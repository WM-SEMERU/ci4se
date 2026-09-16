def nframes(self):
    length = ctypes.c_long()
    size = ctypes.c_int(ctypes.sizeof(length))
    check(_coreaudio.ExtAudioFileGetProperty(self._obj, PROP_LENGTH, ctypes
        .byref(size), ctypes.byref(length)))
    return length.value