def xgroup_setid(self, name, groupname, id):
    return self.execute_command('XGROUP SETID', name, groupname, id)