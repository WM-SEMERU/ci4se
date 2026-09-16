def read(self, size=64, timeout=None):
    if not self._is_open:
        raise HIDException('HIDDevice not open')
    data = [0] * size
    cdata = ffi.new('unsigned char[]', data)
    bytes_read = 0
    if timeout == None:
        bytes_read = hidapi.hid_read(self._device, cdata, len(cdata))
    else:
        bytes_read = hidapi.hid_read_timeout(self._device, cdata, len(cdata
            ), timeout)
    if bytes_read < 0:
        raise HIDException('Failed to read from HID device: ' + str(bytes_read)
            )
    elif bytes_read == 0:
        return []
    else:
        return bytearray(cdata)