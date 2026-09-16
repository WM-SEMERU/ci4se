def _req(self, path, method='get', json=True, assert_status=200, **kw):
    method = getattr(self.session, method.lower())
    res = method(self.url(path), **kw)
    status_code = res.status_code
    if json:
        try:
            res = res.json()
        except ValueError:
            log.error(res.text[:1000])
            raise
    if assert_status:
        if not isinstance(assert_status, (list, tuple)):
            assert_status = [assert_status]
        if status_code not in assert_status:
            log.error('got HTTP %s, expected HTTP %s' % (status_code,
                assert_status))
            log.error(res.text[:1000] if hasattr(res, 'text') else res)
            raise CdstarError('Unexpected HTTP status code', res, status_code)
    return res