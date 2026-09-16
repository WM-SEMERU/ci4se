def translate(self, addr):
    family = socket.getaddrinfo(addr, 0, socket.AF_UNSPEC, socket.SOCK_STREAM)[
        0][0]
    host = socket.getfqdn(addr)
    for a in socket.getaddrinfo(host, 0, family, socket.SOCK_STREAM):
        try:
            return a[4][0]
        except Exception:
            pass
    return addr