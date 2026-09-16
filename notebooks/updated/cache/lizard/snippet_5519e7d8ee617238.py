def calc_crc(self, data, crc=0):
    for char in data:
        crc = crc << 8 ^ self.crctable[(crc >> 8 ^ ord(char)) & 255]
    return crc & 65535