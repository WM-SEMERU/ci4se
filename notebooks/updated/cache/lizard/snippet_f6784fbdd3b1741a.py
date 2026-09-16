def start_user_session(self, username, domain, resource, **kwargs):
    kwargs.setdefault('uptime', pytz.utc.localize(datetime.utcnow()))
    kwargs.setdefault('priority', 0)
    kwargs.setdefault('status', 'online')
    kwargs.setdefault('status_text', '')
    kwargs.setdefault('connection_type', CONNECTION_XMPP)
    kwargs.setdefault('encrypted', True)
    kwargs.setdefault('compressed', False)
    kwargs.setdefault('ip_address', '127.0.0.1')
    if six.PY2 and isinstance(kwargs['ip_address'], str):
        kwargs['ip_address'] = kwargs['ip_address'].decode('utf-8')
    if isinstance(kwargs['ip_address'], six.string_types):
        kwargs['ip_address'] = ipaddress.ip_address(kwargs['ip_address'])
    user = '%s@%s' % (username, domain)
    session = UserSession(self, username, domain, resource, **kwargs)
    data = self.module.get(user)
    if data is None:
        raise UserNotFound(username, domain, resource)
    data.setdefault('sessions', set())
    if isinstance(data['sessions'], list):
        data['sessions'] = set(data['sessions'])
    data['sessions'].add(session)
    self.module.set(user, data)
    all_sessions = self.module.get('all_sessions', set())
    all_sessions.add(session)
    self.module.set('all_sessions', all_sessions)