def describe_security_groups(self, xml_bytes):
    root = XML(xml_bytes)
    result = []
    for group_info in root.findall('securityGroupInfo/item'):
        id = group_info.findtext('groupId')
        name = group_info.findtext('groupName')
        description = group_info.findtext('groupDescription')
        owner_id = group_info.findtext('ownerId')
        allowed_groups = []
        allowed_ips = []
        ip_permissions = group_info.find('ipPermissions')
        if ip_permissions is None:
            ip_permissions = ()
        for ip_permission in ip_permissions:
            ip_protocol = ip_permission.findtext('ipProtocol')
            from_port = ip_permission.findtext('fromPort')
            to_port = ip_permission.findtext('toPort')
            if from_port:
                from_port = int(from_port)
            if to_port:
                to_port = int(to_port)
            for groups in (ip_permission.findall('groups/item') or ()):
                user_id = groups.findtext('userId')
                group_name = groups.findtext('groupName')
                if user_id and group_name:
                    if (user_id, group_name) not in allowed_groups:
                        allowed_groups.append((user_id, group_name))
            for ip_ranges in (ip_permission.findall('ipRanges/item') or ()):
                cidr_ip = ip_ranges.findtext('cidrIp')
                allowed_ips.append(model.IPPermission(ip_protocol,
                    from_port, to_port, cidr_ip))
        allowed_groups = [model.UserIDGroupPair(user_id, group_name) for 
            user_id, group_name in allowed_groups]
        security_group = model.SecurityGroup(id, name, description,
            owner_id=owner_id, groups=allowed_groups, ips=allowed_ips)
        result.append(security_group)
    return result