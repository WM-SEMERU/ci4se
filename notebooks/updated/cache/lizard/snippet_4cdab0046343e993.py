def decode_humidity(packet, channel=1):
    val = str(packet.get(QSDATA, ''))
    if len(val) == 12 and val.startswith('34') and channel == 1:
        humidity = int(val[4:-4], 16)
        return round(float(-6 + 125 * (humidity / pow(2, 16))))
    return None