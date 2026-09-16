def _log_board_ports(self, ports):
    ports = sorted(ports, key=lambda port: (port.tile_id, port.direction))
    self._logln('ports: {0}'.format(' '.join('{}({} {})'.format(p.type.
        value, p.tile_id, p.direction) for p in ports)))