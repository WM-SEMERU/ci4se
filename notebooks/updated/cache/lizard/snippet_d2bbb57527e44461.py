def get_port(self, baud_rate):
    self.port = None
    for test_port in get_serial_ports():
        if self.test_connection(test_port, baud_rate):
            self.port = test_port
            break
        sleep(0.1)
    if self.port is None:
        raise ConnectionError('Could not connect to serial device.')
    return self.port