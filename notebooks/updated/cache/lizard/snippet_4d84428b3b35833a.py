def guess_cls(self):
    try:
        ret = fcntl.ioctl(self.ins, BIOCGDLT, struct.pack('I', 0))
        ret = struct.unpack('I', ret)[0]
    except IOError:
        cls = conf.default_l2
        warning('BIOCGDLT failed: unable to guess type. Using %s !', cls.name)
        return cls
    try:
        return conf.l2types[ret]
    except KeyError:
        cls = conf.default_l2
        warning('Unable to guess type (type %i). Using %s', ret, cls.name)