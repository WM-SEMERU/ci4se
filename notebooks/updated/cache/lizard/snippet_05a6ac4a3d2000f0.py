def decode_temperature(packet, channel=1):
    val = str(packet.get(QSDATA, ''))
    if len(val) == 12 and val.startswith('34') and channel == 1:
        temperature = int(val[-4:], 16)
        return round(float(-46.85 + 175.72 * (temperature / pow(2, 16))))
    return None