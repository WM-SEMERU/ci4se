def _get_close_args(self, data):
    if sys.version_info < (3, 0):
        if not self.on_close or len(inspect.getargspec(self.on_close).args
            ) != 3:
            return []
    elif not self.on_close or len(inspect.getfullargspec(self.on_close).args
        ) != 3:
        return []
    if data and len(data) >= 2:
        code = 256 * six.byte2int(data[0:1]) + six.byte2int(data[1:2])
        reason = data[2:].decode('utf-8')
        return [code, reason]
    return [None, None]