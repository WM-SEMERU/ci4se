def __connect_to_bus(self, bus):

    def connect(bus_num):
        try:
            self.log.debug('Attempting to connect to bus %s...' % bus_num)
            self.bus = smbus.SMBus(bus_num)
            self.log.debug('Success')
        except IOError:
            self.log.debug('Failed')
            raise
    if bus is None:
        try:
            connect(0)
            return
        except IOError:
            pass
        try:
            connect(1)
            return
        except IOError:
            raise
    else:
        try:
            connect(bus)
            return
        except IOError:
            raise