def _get_date(self, decrypted_content):
    date_field = struct.unpack('<5B', decrypted_content[:5])
    dw1 = date_field[0]
    dw2 = date_field[1]
    dw3 = date_field[2]
    dw4 = date_field[3]
    dw5 = date_field[4]
    y = dw1 << 6 | dw2 >> 2
    mon = (dw2 & 3) << 2 | dw3 >> 6
    d = dw3 >> 1 & 31
    h = (dw3 & 1) << 4 | dw4 >> 4
    min_ = (dw4 & 15) << 2 | dw5 >> 6
    s = dw5 & 63
    return datetime(y, mon, d, h, min_, s)