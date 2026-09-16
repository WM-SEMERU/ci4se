def update(self, validate=False):
    rs = self.connection.get_all_snapshots([self.id])
    if len(rs) > 0:
        self._update(rs[0])
    elif validate:
        raise ValueError('%s is not a valid Snapshot ID' % self.id)
    return self.progress