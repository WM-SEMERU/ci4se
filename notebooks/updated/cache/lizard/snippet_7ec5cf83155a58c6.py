def daemon_mode(self, args, options):
    cws = ControlWebSocket(self, args, options)
    cws.start()
    if 'cmdsock' in args and args['cmdsock']:
        lcs = LocalControlSocket(self, args, options)
        lcs.start()
        lcs.join()
    cws.join()