def _bind(l, bind=None):
    if bind is None:
        return
    method = bind.get('method', 'simple')
    if method is None:
        return
    elif method == 'simple':
        l.simple_bind_s(bind.get('dn', ''), bind.get('password', ''))
    elif method == 'sasl':
        sasl_class = getattr(ldap.sasl, bind.get('mechanism', 'EXTERNAL').
            lower())
        creds = bind.get('credentials', None)
        if creds is None:
            creds = {}
        auth = sasl_class(*creds.get('args', []), **creds.get('kwargs', {}))
        l.sasl_interactive_bind_s(bind.get('dn', ''), auth)
    else:
        raise ValueError('unsupported bind method "' + method +
            '"; supported bind methods: simple sasl')