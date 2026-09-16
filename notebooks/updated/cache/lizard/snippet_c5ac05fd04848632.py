def configure_vlan(self, vid, commands):
    commands = make_iterable(commands)
    commands.insert(0, 'vlan %s' % vid)
    return self.configure(commands)