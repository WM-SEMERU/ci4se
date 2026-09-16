def _npcap_set(self, key, val):
    res, code = _exec_cmd(_encapsulate_admin(' '.join([_WlanHelper, self.
        guid[1:-1], key, val])))
    _windows_title()
    if code != 0:
        raise OSError(res.decode('utf8', errors='ignore'))
    return code == 0