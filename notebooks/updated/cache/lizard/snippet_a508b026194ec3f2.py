def status(self):
    try:
        res = self.run(['info'])
        if res[0]['clientName'] == '*unknown*':
            return ConnectionStatus.INVALID_CLIENT
        self.run(['user', '-o'])
    except errors.CommandError as err:
        if 'password (P4PASSWD) invalid or unset' in str(err.args[0]):
            return ConnectionStatus.NO_AUTH
        if 'Connect to server failed' in str(err.args[0]):
            return ConnectionStatus.OFFLINE
    return ConnectionStatus.OK