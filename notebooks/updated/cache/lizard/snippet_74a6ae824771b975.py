def handle_getinfo(self, conn, args):
    result = None
    if args[0] == b'version':
        result = self.version
    elif args[0] == b's2k_count':
        result = '{}'.format(64 << 20).encode('ascii')
    else:
        log.warning('Unknown GETINFO command: %s', args)
    if result:
        keyring.sendline(conn, b'D ' + result)