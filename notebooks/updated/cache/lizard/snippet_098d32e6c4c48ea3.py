def get(self, eid):
    data = self._http_req('connections/%u' % eid)
    self.debug(1, data['decoded'])
    return data['decoded']