def type(self, url=False, text=False, other=None):
    if (url, text, other) == (True, False, None):
        self.ndef_type = _NDEF_URI_TYPE
    elif (url, text, other) == (False, True, None):
        self.ndef_type = _NDEF_TEXT_TYPE
    elif (url, text, type(other)) == (False, False, int):
        self.ndef_type = other
    else:
        raise YubiKeyNEO_USBHIDError('Bad or conflicting NDEF type specified')
    return self