def start(nick, host, port=6667, username=None, password=None, channels=
    None, use_ssl=False, use_sasl=False, char='!', allow_hosts=False,
    allow_nicks=False, disable_query=True):
    client = IRCClient(nick, host, port, username, password, channels or [],
        use_ssl, use_sasl, char, allow_hosts, allow_nicks, disable_query)
    client.io_loop.start()