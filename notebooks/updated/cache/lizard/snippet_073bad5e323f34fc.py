def _get_vpn_status(self):
    sleep(0.3)
    bus = SystemBus()
    ids = []
    for name in self.active:
        conn = bus.get('.NetworkManager', name)
        if conn.Vpn:
            ids.append(conn.Id)
    return ids