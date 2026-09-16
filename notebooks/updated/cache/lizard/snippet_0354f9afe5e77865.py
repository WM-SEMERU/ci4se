def set_owner_params(self, uid=None, gid=None):
    self._set_aliased('uid', uid)
    self._set_aliased('gid', gid)
    return self