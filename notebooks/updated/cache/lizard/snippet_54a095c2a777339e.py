def clear_all_stats(self, *ports):
    port_list = self.set_ports_list(*ports)
    self.api.call_rc('ixClearStats {}'.format(port_list))
    self.api.call_rc('ixClearPacketGroups {}'.format(port_list))