def scan(self):
    devices = []
    diff = 65
    rom = False
    count = 0
    for _ in range(255):
        rom, diff = self._search_rom(rom, diff)
        if rom:
            count += 1
            if count > self.maximum_devices:
                raise RuntimeError('Maximum device count of {} exceeded.'.
                    format(self.maximum_devices))
            devices.append(OneWireAddress(rom))
        if diff == 0:
            break
    return devices