def _read_ipv4_options(self, size=None):
    counter = 0
    optkind = list()
    options = dict()
    while counter < size:
        kind = self._read_unpack(1)
        opts = IPv4_OPT.get(kind)
        if opts is None:
            len_ = size - counter
            counter = size
            options['Unknown'] = self._read_fileng(len_)
            break
        dscp = OPT_TYPE.get(kind)
        desc = dscp.name
        if opts[0]:
            byte = self._read_unpack(1)
            if byte:
                data = process_opt[opts[2]](self, byte, kind)
            else:
                data = dict(kind=kind, type=self._read_opt_type(kind),
                    length=2, flag=True)
        else:
            byte = 1
            data = dict(kind=kind, type=self._read_opt_type(kind), length=1)
        counter += byte
        if dscp in optkind:
            if isinstance(options[desc], tuple):
                options[desc] += Info(data),
            else:
                options[desc] = Info(options[desc]), Info(data)
        else:
            optkind.append(dscp)
            options[desc] = data
        if not kind:
            break
    if counter < size:
        len_ = size - counter
        self._read_binary(len_)
    return tuple(optkind), options