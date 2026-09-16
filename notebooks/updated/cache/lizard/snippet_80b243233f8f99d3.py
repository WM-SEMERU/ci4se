def read_address(self, ip_address):
    title = '%s.read_address' % self.__class__.__name__
    input_fields = {'ip_address': ip_address}
    for key, value in input_fields.items():
        if value:
            object_title = '%s(%s=%s)' % (title, key, str(value))
            self.fields.validate(value, '.%s' % key, object_title)
    self.iam.printer(
        'Querying AWS region %s for properties of elastic ip %s.' % (self.
        iam.region_name, ip_address))
    try:
        response = self.connection.describe_addresses(PublicIps=[ip_address])
        address_info = response['Addresses'][0]
    except:
        raise AWSConnectionError(title)
    address_details = {'instance_id': '', 'public_ip': '', 'allocation_id':
        '', 'association_id': '', 'domain': '', 'network_interface_id': '',
        'network_interface_owner_id': '', 'private_ip_address': '', 'tags':
        [], 'region': self.iam.region_name}
    address_details = self.iam.ingest(address_info, address_details)
    return address_details