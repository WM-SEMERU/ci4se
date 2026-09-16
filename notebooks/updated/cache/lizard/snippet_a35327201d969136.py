def xack(self, name, groupname, *ids):
    return self.execute_command('XACK', name, groupname, *ids)