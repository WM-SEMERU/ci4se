def get_members_of_group(self, gname):
    hostgroup = self.find_by_name(gname)
    if hostgroup:
        return hostgroup.get_hosts()
    return []