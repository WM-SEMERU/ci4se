def temperature(self):
    if not self.awake:
        raise Exception('MPU6050 is in sleep mode, use wakeup()')
    raw = self.i2c_read_register(65, 2)
    raw = struct.unpack('>h', raw)[0]
    return round(raw / 340 + 36.53, 2)