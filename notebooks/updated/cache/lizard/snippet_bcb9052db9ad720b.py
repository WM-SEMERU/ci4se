def recv_exactly(self, n, timeout='default'):
    self._print_recv_header(
        '======== Receiving until exactly {0}B{timeout_text} ========',
        timeout, n)
    return self._recv_predicate(lambda s: n if len(s) >= n else 0, timeout)