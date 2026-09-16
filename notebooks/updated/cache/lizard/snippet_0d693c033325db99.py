def crc16jit(buf, offset, crc, length):
    for index in range(offset, offset + length):
        data = buf[index]
        lookup = crc16_tab[nb.u2(crc) >> 8 & nb.u2(255) ^ data & nb.u2(255)]
        crc = nb.u2(crc) << nb.u2(8) & nb.u2(65535) ^ lookup
        crc = nb.u2(crc) & nb.u2(65535)
    return crc