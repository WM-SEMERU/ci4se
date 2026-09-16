def json_2_subnet(json_obj):
    LOGGER.debug('Subnet.json_2_subnet')
    return Subnet(subnetid=json_obj['subnetID'], name=json_obj['subnetName'
        ], description=json_obj['subnetDescription'], ip=json_obj[
        'subnetIP'], mask=json_obj['subnetMask'], routing_area_id=json_obj[
        'subnetRoutingAreaID'], ip_address_ids=json_obj[
        'subnetIPAddressesID'], subnet_loc_ids=json_obj['subnetLocationsID'
        ], subnet_osi_ids=json_obj['subnetOSInstancesID'])