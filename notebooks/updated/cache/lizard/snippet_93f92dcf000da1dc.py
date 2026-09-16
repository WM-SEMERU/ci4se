def encode(self):
    reading = self.visible_readings[0]
    data = struct.pack('<BBHLLLL', 0, 0, reading.stream, self.origin, self.
        sent_timestamp, reading.raw_time, reading.value)
    return bytearray(data)