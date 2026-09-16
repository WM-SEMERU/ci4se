def resync(self, alias):
    return Zlist(lib.zdir_resync(self._as_parameter_, alias), True)