def parseExtensionArgs(self, args, is_openid1, strict=False):
    policies_str = args.get('auth_policies')
    if policies_str:
        auth_policies = policies_str.split(' ')
    elif strict:
        raise ValueError('Missing auth_policies')
    else:
        auth_policies = []
    if len(auth_policies) > 1 and strict and AUTH_NONE in auth_policies:
        raise ValueError(
            'Got some auth policies, as well as the special "none" URI: %r' %
            (auth_policies,))
    if 'none' in auth_policies:
        msg = '"none" used as a policy URI (see PAPE draft < 5)'
        if strict:
            raise ValueError(msg)
        else:
            warnings.warn(msg, stacklevel=2)
    auth_policies = [u for u in auth_policies if u not in ['none', AUTH_NONE]]
    self.auth_policies = auth_policies
    for key, val in args.iteritems():
        if key.startswith('auth_level.'):
            alias = key[11:]
            if alias.startswith('ns.'):
                continue
            try:
                uri = args['auth_level.ns.%s' % (alias,)]
            except KeyError:
                if is_openid1:
                    uri = self._default_auth_level_aliases.get(alias)
                else:
                    uri = None
            if uri is None:
                if strict:
                    raise ValueError('Undefined auth level alias: %r' % (
                        alias,))
            else:
                self.setAuthLevel(uri, val, alias)
    auth_time = args.get('auth_time')
    if auth_time:
        if TIME_VALIDATOR.match(auth_time):
            self.auth_time = auth_time
        elif strict:
            raise ValueError('auth_time must be in RFC3339 format')