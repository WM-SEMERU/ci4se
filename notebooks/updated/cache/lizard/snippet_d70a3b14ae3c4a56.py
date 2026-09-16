def get_feature_report(self, size, report_id=0):
    data = [0] * (size + 1)
    cdata = ffi.new('unsigned char[]', bytes(data))
    cdata[0] = report_id
    bytes_read = hidapi.hid_get_feature_report(self._device, cdata, len(cdata))
    if bytes_read == -1:
        raise HIDException('Failed to get feature report from HID device')
    return bytearray(cdata[1:size + 1])