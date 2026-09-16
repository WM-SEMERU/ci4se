def _read_bytes_from_socket(self, msglen):
    chunks = []
    bytes_recd = 0
    while bytes_recd < msglen:
        if self.stop.is_set():
            raise InterruptLoop('Stopped while reading from socket')
        try:
            chunk = self.socket.recv(min(msglen - bytes_recd, 2048))
            if chunk == b'':
                raise socket.error('socket connection broken')
            chunks.append(chunk)
            bytes_recd += len(chunk)
        except socket.timeout:
            continue
        except ssl.SSLError as exc:
            if _is_ssl_timeout(exc):
                continue
            raise
    return b''.join(chunks)