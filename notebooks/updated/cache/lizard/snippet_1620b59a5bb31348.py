def send_packet(self, packet):
    data = json.dumps(packet)
    byte = data.encode('utf-8')
    self.udp_socket.sendto(byte, (self._host, self._udp_port))