def size(self):
    if self._check_hash_view():
        return 1
    else:
        return self.engine.open().view.size(xmlrpc.NOHASH, self.viewname)