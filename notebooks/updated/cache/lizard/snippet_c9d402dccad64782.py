def parse_next(self, ptype, m):
    if ptype == MSG_KEXGSS_GROUPREQ:
        return self._parse_kexgss_groupreq(m)
    elif ptype == MSG_KEXGSS_GROUP:
        return self._parse_kexgss_group(m)
    elif ptype == MSG_KEXGSS_INIT:
        return self._parse_kexgss_gex_init(m)
    elif ptype == MSG_KEXGSS_HOSTKEY:
        return self._parse_kexgss_hostkey(m)
    elif ptype == MSG_KEXGSS_CONTINUE:
        return self._parse_kexgss_continue(m)
    elif ptype == MSG_KEXGSS_COMPLETE:
        return self._parse_kexgss_complete(m)
    elif ptype == MSG_KEXGSS_ERROR:
        return self._parse_kexgss_error(m)
    msg = 'KexGex asked to handle packet type {:d}'
    raise SSHException(msg.format(ptype))