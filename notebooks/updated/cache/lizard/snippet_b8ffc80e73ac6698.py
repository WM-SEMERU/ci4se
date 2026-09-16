def _init_cfg_interfaces(self, cb, intf_list=None, all_intf=True):
    if not all_intf:
        self.intf_list = intf_list
    else:
        self.intf_list = sys_utils.get_all_run_phy_intf()
    self.cb = cb
    self.intf_attr = {}
    self.cfg_lldp_interface_list(self.intf_list)