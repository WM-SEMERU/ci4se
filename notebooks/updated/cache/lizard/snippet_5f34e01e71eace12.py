def decode_imod(packet, channel=1):
    val = str(packet.get(QSDATA, ''))
    if len(val) == 8 and val.startswith('4e'):
        try:
            _map = ((5, 1), (5, 2), (5, 4), (4, 1), (5, 1), (5, 2))[channel - 1
                ]
            return int(val[_map[0]], 16) & _map[1] == 0
        except IndexError:
            return None
    return None