def buildCliString(self):
    config = self.navbar.getActiveConfig()
    group = self.buildSpec['widgets'][self.navbar.getSelectedGroup()]
    positional = config.getPositionalArgs()
    optional = config.getOptionalArgs()
    print(cli.buildCliString(self.buildSpec['target'], group['command'],
        positional, optional))
    return cli.buildCliString(self.buildSpec['target'], group['command'],
        positional, optional)