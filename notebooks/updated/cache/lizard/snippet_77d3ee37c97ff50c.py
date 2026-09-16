def command_health(self):
    if len(self.args) == 1 and self.args[0] == 'health':
        PackageHealth(mode='').test()
    elif len(self.args) == 2 and self.args[0] == 'health' and self.args[1
        ] == '--silent':
        PackageHealth(mode=self.args[1]).test()
    else:
        usage('')