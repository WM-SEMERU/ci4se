def packetToDict(pkt):
    d = {'id': pkt[4], 'instruction': xl320.InstrToStr[pkt[7]], 'length': (
        pkt[6] << 8) + pkt[5], 'params': pkt[8:-2], 'crc': pkt[-2:]}
    return d