def create_subnet(self, vpc_id, cidr_block, availability_zone=None):
    params = {'VpcId': vpc_id, 'CidrBlock': cidr_block}
    if availability_zone:
        params['AvailabilityZone'] = availability_zone
    return self.get_object('CreateSubnet', params, Subnet)