def fill(self, address, data, size, x, y, p):
    if size % 4 or address % 4:
        data = struct.pack('<B', data) * size
        self.write(address, data, x, y, p)
    else:
        self._send_scp(x, y, p, SCPCommands.fill, address, data, size)