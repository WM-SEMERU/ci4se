def pack_ip_addr(addr):
    addr, port = addr
    return socket.inet_aton(addr) + struct.pack('!H', port & _short_mask)