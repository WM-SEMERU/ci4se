def create_security_group(self, name, description, vpc_id=None):
    params = {'GroupName': name, 'GroupDescription': description}
    if vpc_id is not None:
        params['VpcId'] = vpc_id
    group = self.get_object('CreateSecurityGroup', params, SecurityGroup,
        verb='POST')
    group.name = name
    group.description = description
    return group