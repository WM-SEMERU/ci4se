def Command(cls, usb, service, command='', timeout_ms=None):
    return ''.join(cls.StreamingCommand(usb, service, command, timeout_ms))