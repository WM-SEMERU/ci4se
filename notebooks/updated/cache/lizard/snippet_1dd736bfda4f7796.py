def recalculate_spanning_tree(self, init=True):
    for port in self.ports.values():
        if port.state is not PORT_STATE_DISABLE:
            port.down(PORT_STATE_BLOCK, msg_init=init)
    if init:
        self.send_event(EventTopologyChange(self.dp))
    port_roles = {}
    self.root_priority = Priority(self.bridge_id, 0, None, None)
    self.root_times = self.bridge_times
    if init:
        self.logger.info('Root bridge.', extra=self.dpid_str)
        for port_no in self.ports:
            port_roles[port_no] = DESIGNATED_PORT
    else:
        port_roles, self.root_priority, self.root_times = (self.
            _spanning_tree_algorithm())
    for port_no, role in port_roles.items():
        if self.ports[port_no].state is not PORT_STATE_DISABLE:
            self.ports[port_no].up(role, self.root_priority, self.root_times)