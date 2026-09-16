def hexraw(self, lfilter=None):
    for i, res in enumerate(self.res):
        p = self._elt2pkt(res)
        if lfilter is not None and not lfilter(p):
            continue
        print('%s %s %s' % (conf.color_theme.id(i, fmt='%04i'), p.sprintf(
            '%.time%'), self._elt2sum(res)))
        if p.haslayer(conf.raw_layer):
            hexdump(p.getlayer(conf.raw_layer).load)