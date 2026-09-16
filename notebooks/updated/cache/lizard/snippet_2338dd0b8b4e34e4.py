def cancel_port_forward(self, address, port):
    if not self.active:
        return
    self._tcp_handler = None
    self.global_request('cancel-tcpip-forward', (address, port), wait=True)