def _update_port_group_info(self, switches=None):
    if switches is None:
        switches = self._switches.keys()
    for switch_ip in switches:
        client = self._switches.get(switch_ip)
        ret = self._run_eos_cmds(['show interfaces'], client)
        if not ret or len(ret) == 0:
            LOG.warning('Unable to retrieve interface info for %s', switch_ip)
            continue
        intf_info = ret[0]
        self._port_group_info[switch_ip] = intf_info.get('interfaces', {})