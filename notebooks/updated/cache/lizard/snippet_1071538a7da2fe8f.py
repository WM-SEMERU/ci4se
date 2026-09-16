def parse(self, data):
    self.validate_packet(data)
    id_ = self.dump_hex(data[4:6])
    temperature = ((data[6] & 127) * 256 + data[7]) / 10
    signbit = data[6] & 128
    if signbit != 0:
        temperature = -temperature
    sensor_specific = {'id': id_, 'temperature': temperature}
    results = self.parse_header_part(data)
    results.update(RfxPacketUtils.parse_signal_and_battery(data[8]))
    results.update(sensor_specific)
    return results