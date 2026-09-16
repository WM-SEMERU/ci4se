def add_bond(self, name, ifaces, bond_mode=None, lacp=None):
    assert len(ifaces) >= 2
    options = ''
    if bond_mode:
        options += 'bond_mode=%(bond_mode)s' % locals()
    if lacp:
        options += 'lacp=%(lacp)s' % locals()
    command_add = ovs_vsctl.VSCtlCommand('add-bond', (self.br_name, name,
        ifaces), options)
    self.run_command([command_add])