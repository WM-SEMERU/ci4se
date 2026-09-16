def readAccelRange(self):
    raw_data = self._readByte(self.REG_ACCEL_CONFIG)
    raw_data = (raw_data | 231) ^ 231
    return raw_data