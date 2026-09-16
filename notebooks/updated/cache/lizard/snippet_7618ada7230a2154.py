def list_vrf(self, auth, spec=None):
    if spec is None:
        spec = {}
    self._logger.debug('list_vrf called; spec: %s' % unicode(spec))
    sql = 'SELECT * FROM ip_net_vrf'
    params = list()
    if spec is not None and not {}:
        where, params = self._expand_vrf_spec(spec)
    if len(params) > 0:
        sql += ' WHERE ' + where
    sql += ' ORDER BY vrf_rt_order(rt) NULLS FIRST'
    self._execute(sql, params)
    res = list()
    for row in self._curs_pg:
        res.append(dict(row))
    return res