def serialize(self):
    commands = []
    for cmd in self.commands:
        commands.append(cmd.serialize())
    out = {'commands': commands, 'deviceURL': self.__device_url}
    return out