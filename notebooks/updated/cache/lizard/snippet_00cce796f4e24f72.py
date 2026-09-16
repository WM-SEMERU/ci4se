def stop(self, host, port):
    args = {'host': host, 'port': port}
    self._rtinfo_stop_params_chk.check(args)
    return self._client.json('rtinfo.stop', args)