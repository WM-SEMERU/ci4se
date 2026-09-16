def connect(self, interface=None):
    if self._simulate:
        return True
    if not interface:
        match = self._autodiscover_usb()
        self._log.debug('Auto-discovered USB port: %s' % match)
    else:
        self.USB_PORT = interface
    try:
        self._conn = serial.Serial(self.USB_PORT, baudrate=self.BAUDRATE,
            bytesize=self.BYTE_SIZE, parity=self.PARITY, stopbits=self.
            STOPBITS, timeout=self.TIMEOUT)
    except serial.serialutil.SerialException as e:
        raise SerialConnectionError(str(e))
    self._log.debug('Serial connection set')
    if not self._conn.isOpen():
        self._conn.open()
        self._log.debug('Serial connection opened')
    return True