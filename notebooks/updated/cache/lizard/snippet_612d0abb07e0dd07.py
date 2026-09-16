def get_groupnames(self, hostgroups):
    group_names = []
    for hostgroup_id in self.hostgroups:
        hostgroup = hostgroups[hostgroup_id]
        group_names.append(hostgroup.get_name())
    return ','.join(sorted(group_names))