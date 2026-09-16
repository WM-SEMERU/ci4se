def _get_bridge_name(self):
    command = ovs_vsctl.VSCtlCommand('find', ('Bridge', 'datapath_id=%s' %
        dpid_lib.dpid_to_str(self.datapath_id)))
    self.run_command([command])
    if not isinstance(command.result, list) or len(command.result) != 1:
        raise OVSBridgeNotFound(datapath_id=dpid_lib.dpid_to_str(self.
            datapath_id))
    return command.result[0].name