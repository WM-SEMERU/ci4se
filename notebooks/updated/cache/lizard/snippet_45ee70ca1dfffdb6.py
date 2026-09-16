def del_port(self, port_name):
    command = ovs_vsctl.VSCtlCommand('del-port', (self.br_name, port_name))
    self.run_command([command])