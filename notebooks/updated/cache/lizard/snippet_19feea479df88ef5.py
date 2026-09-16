def send_packet(self, packet, protocol='json', time_precision=None):
    if protocol == 'json':
        data = make_lines(packet, time_precision).encode('utf-8')
    elif protocol == 'line':
        data = ('\n'.join(packet) + '\n').encode('utf-8')
    self.udp_socket.sendto(data, (self._host, self._udp_port))