def touch(self, key, expire=0, noreply=None):
    if noreply is None:
        noreply = self.default_noreply
    key = self.check_key(key)
    cmd = b'touch ' + key + b' ' + six.text_type(expire).encode('ascii')
    if noreply:
        cmd += b' noreply'
    cmd += b'\r\n'
    results = self._misc_cmd([cmd], b'touch', noreply)
    if noreply:
        return True
    return results[0] == b'TOUCHED'