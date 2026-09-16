def from_bytes(cls, bitstream):
    packet = cls()
    if not isinstance(bitstream, ConstBitStream):
        if isinstance(bitstream, Bits):
            bitstream = ConstBitStream(auto=bitstream)
        else:
            bitstream = ConstBitStream(bytes=bitstream)
    type_nr = bitstream.read('uint:4')
    if type_nr != packet.message_type:
        msg = 'Invalid bitstream for a {0} packet'
        class_name = packet.__class__.__name__
        raise ValueError(msg.format(class_name))
    packet._reserved1 = bitstream.read(20)
    record_count = bitstream.read('uint:8')
    packet.nonce = bitstream.read('bytes:8')
    for dummy in range(record_count):
        record = MapReferralRecord.from_bytes(bitstream)
        packet.records.append(record)
    packet.sanitize()
    return packet