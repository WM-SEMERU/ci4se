def send(self, s):
    self._print_header('======== Sending ({0}) ========'.format(len(s)))
    self._log_send(s)
    out = len(s)
    while s:
        s = s[self._send(s):]
    return out