def capabilityCheck(self, optional=None, required=None):
    res = self.query('version', {'optional': optional or [], 'required': 
        required or []})
    if not self._hasprop(res, 'capabilities'):
        capabilities.synthesize(res, optional)
        if 'error' in res:
            raise CommandError(res['error'])
    return res