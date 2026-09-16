def i2m(self, pkt, i):
    mask, ip = i
    ip = socket.inet_aton(ip)
    return struct.pack('>B', mask) + ip[:self.mask2iplen(mask)]