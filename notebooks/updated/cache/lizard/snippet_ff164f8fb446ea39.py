def RequestPacket(self):
    attr = self._PktEncodeAttributes()
    if self.id is None:
        self.id = self.CreateID()
    header = struct.pack('!BBH', self.code, self.id, 20 + len(attr))
    self.authenticator = md5_constructor(header[0:4] + 16 * six.b('\x00') +
        attr + self.secret).digest()
    return header + self.authenticator + attr