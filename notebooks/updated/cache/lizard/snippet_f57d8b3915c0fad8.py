def size(self):
    width = c_double(0)
    height = c_double(0)
    rc = self._libinput.libinput_device_get_size(self._handle, byref(width),
        byref(height))
    assert rc == 0, 'This device does not provide size information'
    return width.value, height.value