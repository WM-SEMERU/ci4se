def parse_next(self, ptype, m):
    if self.transport.server_mode and ptype == MSG_KEXGSS_INIT:
        return self._parse_kexgss_init(m)
    elif not self.transport.server_mode and ptype == MSG_KEXGSS_HOSTKEY:
        return self._parse_kexgss_hostkey(m)
    elif self.transport.server_mode and ptype == MSG_KEXGSS_CONTINUE:
        return self._parse_kexgss_continue(m)
    elif not self.transport.server_mode and ptype == MSG_KEXGSS_COMPLETE:
        return self._parse_kexgss_complete(m)
    elif ptype == MSG_KEXGSS_ERROR:
        return self._parse_kexgss_error(m)
    msg = 'GSS KexGroup1 asked to handle packet type {:d}'
    raise SSHException(msg.format(ptype))