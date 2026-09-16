def _read(self):
    request_type = _USB_TYPE_CLASS | _USB_RECIP_INTERFACE | _USB_ENDPOINT_IN
    value = _REPORT_TYPE_FEATURE << 8
    recv = self._usb_handle.controlMsg(request_type, _HID_GET_REPORT,
        _FEATURE_RPT_SIZE, value=value, timeout=_USB_TIMEOUT_MS)
    if len(recv) != _FEATURE_RPT_SIZE:
        self._debug(
            'Failed reading %i bytes (got %i) from USB HID YubiKey.\n' % (
            _FEATURE_RPT_SIZE, recv))
        raise YubiKeyUSBHIDError('Failed reading from USB HID YubiKey')
    data = b''.join(yubico_util.chr_byte(c) for c in recv)
    self._debug('READ  : %s' % yubico_util.hexdump(data, colorize=True))
    return data