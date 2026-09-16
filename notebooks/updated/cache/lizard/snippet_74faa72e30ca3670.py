def parse(self):
    if len(self.raw_data) < 3:
        ValueError(
            'parse() may only be called on a frame containing at least 3 bytes of raw data (see fill())'
            )
    raw_len = self.raw_data[1:3]
    data_len = struct.unpack('> h', raw_len)[0]
    data = self.raw_data[3:3 + data_len]
    chksum = self.raw_data[-1]
    self.data = data
    if not self.verify(chksum):
        raise ValueError('Invalid checksum')