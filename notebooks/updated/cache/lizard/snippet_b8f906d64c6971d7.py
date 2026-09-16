def knx2_to_float(knxdata):
    if len(knxdata) != 2:
        raise KNXException('Can only convert a 2 Byte object to float')
    data = knxdata[0] * 256 + knxdata[1]
    sign = data >> 15
    exponent = data >> 11 & 15
    mantisse = float(data & 2047)
    if sign == 1:
        mantisse = -2048 + mantisse
    return mantisse * pow(2, exponent) / 100