def _connect(self):
    port = utils.find_device('1A86:5523')
    wait_timeout = time.time() + 40.0
    self._connect_state.value = self.CS_CONNECTING
    connect_success = False
    while time.time() < wait_timeout:
        try:
            self._ser = serial.Serial(port=port, baudrate=9600, bytesize=8,
                parity='N', stopbits=1.5, timeout=0.25, xonxoff=False,
                rtscts=False, dsrdtr=False)
            connect_success = True
            break
        except serial.SerialException:
            time.sleep(0.5)
    if not connect_success:
        raise exceptions.RoasterLookupError
    self._initialize()