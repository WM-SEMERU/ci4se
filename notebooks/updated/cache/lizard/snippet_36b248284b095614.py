def process_raw_data(cls, raw_data):
    properties = raw_data['properties']
    raw_content = properties.get('addressSpace', None)
    if raw_content is not None:
        address_space = AddressSpace.from_raw_data(raw_content)
        properties['addressSpace'] = address_space
    raw_content = properties.get('dhcpOptions')
    if raw_content is not None:
        dhcp_options = DHCPOptions.from_raw_data(raw_content)
        properties['dhcpOptions'] = dhcp_options
    raw_content = properties.get('logicalNetwork', None)
    if raw_content is not None:
        properties['logicalNetwork'] = Resource.from_raw_data(raw_content)
    subnetworks = []
    for raw_subnet in properties.get('subnets', []):
        raw_subnet['parentResourceID'] = raw_data['resourceId']
        subnetworks.append(SubNetworks.from_raw_data(raw_subnet))
    properties['subnets'] = subnetworks
    return super(VirtualNetworks, cls).process_raw_data(raw_data)