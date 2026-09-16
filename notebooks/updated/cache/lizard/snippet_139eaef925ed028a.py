def _get_anon_bind(self):
    r = self._search('cn=config', '(objectClass=*)', [
        'nsslapd-allow-anonymous-access'], scope=ldap.SCOPE_BASE)
    dn, attrs = r[0]
    state = attrs.get('nsslapd-allow-anonymous-access')[0].decode('utf-8',
        'ignore')
    if state in ['on', 'off', 'rootdse']:
        r = state
    else:
        r = None
    self._anon_bind = r