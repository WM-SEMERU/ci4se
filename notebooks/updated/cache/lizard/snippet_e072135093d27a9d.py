def _set_slave_enabled(self, dpid, port, enabled):
    slave = self._get_slave(dpid, port)
    if slave:
        slave['enabled'] = enabled