def get_mac(self):
    ifreq = struct.pack('16sH14s', self.name, AF_UNIX, b'\x00' * 14)
    res = fcntl.ioctl(sockfd, SIOCGIFHWADDR, ifreq)
    address = struct.unpack('16sH14s', res)[2]
    mac = struct.unpack('6B8x', address)
    return ':'.join([('%02X' % i) for i in mac])