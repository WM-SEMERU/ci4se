def is_limited(self, identifier):
    if identifier in self._limits:
        limit, blocking = self._limits[identifier]
        if time() < limit:
            self._log.debug('Global limit enforced for Object {oid}'.format
                (oid=id(identifier)))
            if blocking:
                raise LimitError
            return True
        else:
            del self._limits[identifier]
    self._log.debug('No global limit enforced for Object {oid}'.format(oid=
        id(identifier)))
    return False