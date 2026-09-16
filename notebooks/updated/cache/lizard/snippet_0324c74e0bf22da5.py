def execute_command(self, cmd, params=None, callback=None, raw=False):

    def execute_with_callbacks(cmd, params=None, callback=None, raw=False):
        code, params = self.send_command(cmd, params, raw)
        if callback:
            callback(code, params)
        return code, params
    if self.daemon:
        t = Thread(target=execute_with_callbacks, args=(cmd,), kwargs={
            'params': params, 'callback': callback, 'raw': raw})
        t.daemon = True
        t.start()
    else:
        return execute_with_callbacks(cmd, params, callback, raw)