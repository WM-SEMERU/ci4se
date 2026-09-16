def remove_pool(self, auth, spec):
    self._logger.debug('remove_pool called; spec: %s' % unicode(spec))
    pools = self.list_pool(auth, spec)
    where, params = self._expand_pool_spec(spec)
    sql = 'DELETE FROM ip_net_pool AS po WHERE %s' % where
    self._execute(sql, params)
    audit_params = {'username': auth.username, 'authenticated_as': auth.
        authenticated_as, 'full_name': auth.full_name,
        'authoritative_source': auth.authoritative_source}
    for p in pools:
        audit_params['pool_id'] = p['id'],
        audit_params['pool_name'] = p['name'],
        audit_params['description'] = 'Removed pool %s' % p['name']
        sql, params = self._sql_expand_insert(audit_params)
        self._execute('INSERT INTO ip_net_log %s' % sql, params)