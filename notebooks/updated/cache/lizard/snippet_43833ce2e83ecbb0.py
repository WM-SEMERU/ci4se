def config(self, handle, attributes=None, **kwattrs):
    self._check_session()
    if kwattrs:
        if attributes:
            attributes.update(kwattrs)
        else:
            attributes = kwattrs
    self._rest.put_request('objects', str(handle), attributes)