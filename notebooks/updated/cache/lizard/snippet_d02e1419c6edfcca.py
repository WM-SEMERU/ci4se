def decode_wireformat_uuid(rawguid):
    if isinstance(rawguid, list):
        rawguid = bytearray(rawguid)
    lebytes = struct.unpack_from('<IHH', buffer(rawguid[:8]))
    bebytes = struct.unpack_from('>HHI', buffer(rawguid[8:]))
    return '{0:08X}-{1:04X}-{2:04X}-{3:04X}-{4:04X}{5:08X}'.format(lebytes[
        0], lebytes[1], lebytes[2], bebytes[0], bebytes[1], bebytes[2])