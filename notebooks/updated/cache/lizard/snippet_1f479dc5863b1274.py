def add_serverconnection_methods(cls):
    methods = ['action', 'admin', 'cap', 'ctcp', 'ctcp_reply', 'globops',
        'info', 'invite', 'ison', 'join', 'kick', 'links', 'list', 'lusers',
        'mode', 'motd', 'names', 'nick', 'notice', 'oper', 'part', 'part',
        'pass_', 'ping', 'pong', 'privmsg', 'privmsg_many', 'quit',
        'send_raw', 'squit', 'stats', 'time', 'topic', 'trace', 'user',
        'userhost', 'users', 'version', 'wallops', 'who', 'whois', 'whowas']
    for m in methods:
        method = _wrap_execute_after(m)
        f = getattr(irc.client.ServerConnection, m)
        method.__doc__ = f.__doc__
        setattr(cls, method.__name__, method)
    return cls