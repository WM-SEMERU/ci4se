def _set_and_filter(self):
    fmtos = []
    seen = set()
    for key in self._force:
        self._registered_updates.setdefault(key, getattr(self, key).value)
    for key, value in chain(six.iteritems(self._registered_updates), six.
        iteritems({key: getattr(self, key).default for key in self}) if
        self._todefault else ()):
        if key in seen:
            continue
        seen.add(key)
        fmto = getattr(self, key)
        if key in self._shared and key not in self._force:
            if not self._shared[key].plotter._updating:
                warn(
                    '%s formatoption is shared with another plotter. Use the unshare method to enable the updating'
                     % fmto.key, logger=self.logger)
            changed = False
        else:
            try:
                changed = fmto.check_and_set(value, todefault=self.
                    _todefault, validate=not self.no_validation)
            except Exception as e:
                self._registered_updates.pop(key, None)
                self.logger.debug('Failed to set %s', key)
                raise e
        changed = changed or key in self._force
        if changed:
            fmtos.append(fmto)
    fmtos = self._insert_additionals(fmtos, seen)
    for fmto in fmtos:
        fmto.lock.acquire()
    self._todefault = False
    self._registered_updates.clear()
    self._force.clear()
    return fmtos