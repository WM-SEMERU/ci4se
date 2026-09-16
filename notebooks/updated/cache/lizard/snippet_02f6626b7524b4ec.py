def linkify_hostgroups_hosts(self, hosts):
    for hostgroup in self:
        members = hostgroup.get_hosts()
        new_members = []
        for member in members:
            member = member.strip()
            if not member:
                continue
            if member == '*':
                new_members.extend(list(hosts.items.keys()))
            else:
                host = hosts.find_by_name(member)
                if host is not None:
                    new_members.append(host.uuid)
                    if hostgroup.uuid not in host.hostgroups:
                        host.hostgroups.append(hostgroup.uuid)
                else:
                    hostgroup.add_unknown_members(member)
        new_members = list(set(new_members))
        hostgroup.replace_members(new_members)