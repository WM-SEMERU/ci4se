def post_build(self, packet, payload):
    if self.records_number is None:
        recnum = struct.pack('!H', len(self.records))
        packet = packet[:6] + recnum + packet[8:]
    return _ICMPv6.post_build(self, packet, payload)