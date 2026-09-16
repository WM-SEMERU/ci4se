def _lease_valid(self, lease):
    if not lease.exist:
        return None
    if lease.has_env:
        return lease.uuid_path
    else:
        self._release(lease)
        return None