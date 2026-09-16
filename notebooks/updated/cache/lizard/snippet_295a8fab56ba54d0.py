def set_ipv4(self, ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bin_ip = socket.inet_aton(ip)
    ifreq = struct.pack('16sH2s4s8s', self.name, socket.AF_INET, '\x00' * 2,
        bin_ip, '\x00' * 8)
    fcntl.ioctl(sock, self.SIOCSIFADDR, ifreq)
    ifreq = struct.pack('16sH', self.name, self.IFF_UP | self.
        IFF_POINTOPOINT | self.IFF_RUNNING | self.IFF_MULTICAST)
    fcntl.ioctl(sock, self.SIOCSIFFLAGS, ifreq)