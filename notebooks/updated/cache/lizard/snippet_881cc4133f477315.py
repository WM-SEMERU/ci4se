def keyEvent(self, key, down=1):
    self.transport.write(pack('!BBxxI', 4, down, key))