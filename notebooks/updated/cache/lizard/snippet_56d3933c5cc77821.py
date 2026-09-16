def get_my_feed(self, limit=150, offset=20, sort='updated', nid=None):
    r = self.request(method='network.get_my_feed', nid=nid, data=dict(limit
        =limit, offset=offset, sort=sort))
    return self._handle_error(r, 'Could not retrieve your feed.')