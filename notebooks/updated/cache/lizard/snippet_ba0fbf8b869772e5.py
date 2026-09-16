def add_server(self, name, prefer=False):
    if not name or re.match('^[\\s]+$', name):
        raise ValueError('ntp server name must be specified')
    if prefer:
        name = '%s prefer' % name
    cmd = self.command_builder('ntp server', value=name)
    return self.configure(cmd)