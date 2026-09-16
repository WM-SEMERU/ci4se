def _send_queries(self):
    res = 0
    addrs = _resolve_addrs(self.addresses, self.port, self.
        ignore_senderrors, [self._sock.family])
    for addr in addrs:
        try:
            self._send_query(addr[1])
            res += 1
        except:
            if not self.ignore_senderrors:
                raise
    return res