def _metahash(self):
    if self._cached_metahash:
        return self._cached_metahash
    mhash = base.BaseBuilder._metahash(self)
    log.debug('[%s]: Metahash input: cmd="%s"', self.address, self.cmd)
    mhash.update(self.cmd)
    self._cached_metahash = mhash
    return mhash