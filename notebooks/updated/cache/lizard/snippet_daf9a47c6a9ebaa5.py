def connect(self, attempts=20, delay=0.5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    with closing(sock):
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        discover_packet = build_packet(REQ_GATEWAY, ALL_BULBS, ALL_BULBS,
            '', protocol=DISCOVERY_PROTOCOL)
        for _, ok in _retry(self.gateway_found_event, attempts, delay):
            sock.sendto(discover_packet, BROADCAST_ADDRESS)
    if not ok:
        raise ConnectException('discovery failed')
    self.callbacks.put(EVENT_DISCOVERED)
    for _, ok in _retry(self.sender.is_connected, 1, 3):
        self.sender.put(self.gateway)
    if not ok:
        raise ConnectException('connection failed')
    self.callbacks.put(EVENT_CONNECTED)
    for _, ok in _retry(self.bulbs_found_event, attempts, delay):
        self.send(REQ_GET_LIGHT_STATE, ALL_BULBS, '')
    if not ok:
        raise ConnectException('only found %d of %d bulbs' % (len(self.
            bulbs), self.num_bulbs))
    self.callbacks.put(EVENT_BULBS_FOUND)