def decode_pir(packet, channel=1):
    val = str(packet.get(QSDATA, ''))
    if len(val) == 8 and val.startswith('0f') and channel == 1:
        return int(val[-4:], 16) > 0
    return None