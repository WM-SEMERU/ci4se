def modify(self, api_action, sgid, other, proto_spec):
    params = {'group_id': sgid, 'ip_permissions': []}
    perm = {}
    params['ip_permissions'].append(perm)
    proto, from_port, to_port = proto_spec
    perm['IpProtocol'] = proto
    perm['FromPort'] = from_port or 0
    perm['ToPort'] = to_port or from_port or 65535
    if other.startswith('sg-'):
        perm['UserIdGroupPairs'] = [{'GroupId': other}]
    elif '/sg-' in other:
        account, group_id = other.split('/', 1)
        perm['UserIdGroupPairs'] = [{'UserId': account, 'GroupId': group_id}]
    else:
        perm['IpRanges'] = [{'CidrIp': other}]
    return self.call(api_action, **params)