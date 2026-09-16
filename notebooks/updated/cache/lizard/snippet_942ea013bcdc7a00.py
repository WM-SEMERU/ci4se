def do_get(self, params):
    watcher = lambda evt: self.show_output(str(evt))
    kwargs = {'watch': watcher} if params.watch else {}
    value, _ = self._zk.get(params.path, **kwargs)
    if value is not None:
        try:
            value = zlib.decompress(value)
        except:
            pass
    self.show_output(value)