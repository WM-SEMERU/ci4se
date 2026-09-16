def _load_properties(self, raw_bytes):
    r = AMQPReader(raw_bytes)
    flags = []
    while 1:
        flag_bits = r.read_short()
        flags.append(flag_bits)
        if flag_bits & 1 == 0:
            break
    shift = 0
    d = {}
    for key, proptype in self.PROPERTIES:
        if shift == 0:
            if not flags:
                break
            flag_bits, flags = flags[0], flags[1:]
            shift = 15
        if flag_bits & 1 << shift:
            d[key] = getattr(r, 'read_' + proptype)()
        shift -= 1
    self.properties = d