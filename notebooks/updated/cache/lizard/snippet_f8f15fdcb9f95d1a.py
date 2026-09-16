def run_cmd(self, *args, **kwargs):
    timeout = kwargs.pop('timeout', None)
    p = self.raw_cmd(*args, **kwargs)
    return p.communicate(timeout=timeout)[0].decode('utf-8').replace('\r\n',
        '\n')