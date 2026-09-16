def _recv_all(self, size):
    r_buffer = bytes()
    while len(r_buffer) < size:
        r_packet = self._recv(size - len(r_buffer))
        if not r_packet:
            return None
        r_buffer += r_packet
    return r_buffer