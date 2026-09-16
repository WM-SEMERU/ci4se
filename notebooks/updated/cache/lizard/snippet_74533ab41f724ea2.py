def keys(self, remote=False):
    if not remote:
        return list(super(CouchDB, self).keys())
    return self.all_dbs()