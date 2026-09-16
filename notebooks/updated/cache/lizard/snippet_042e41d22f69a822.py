def execute(self, model, method, *args):
    self._check_logged_user()
    args_to_send = [self.env.db, self.env.uid, self._password, model, method]
    args_to_send.extend(args)
    data = self.json('/jsonrpc', {'service': 'object', 'method': 'execute',
        'args': args_to_send})
    return data.get('result')