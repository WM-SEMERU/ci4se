def create(self, vrf_name, rd=None):
    commands = ['vrf definition %s' % vrf_name]
    if rd:
        commands.append('rd %s' % rd)
    return self.configure(commands)