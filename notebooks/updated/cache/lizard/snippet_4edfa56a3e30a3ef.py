def get(self, name):
    if not isvalidinterface(name):
        return None
    config = self.get_block('^interface\\s%s$' % name)
    resp = dict()
    resp.update(self._parse_bpduguard(config))
    resp.update(self._parse_portfast(config))
    resp.update(self._parse_portfast_type(config))
    return resp