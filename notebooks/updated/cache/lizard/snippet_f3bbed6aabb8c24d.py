def list_availability_zones(call=None):
    ret = {}
    params = {'Action': 'DescribeZones', 'RegionId': get_location()}
    items = query(params)
    for zone in items['Zones']['Zone']:
        ret[zone['ZoneId']] = {}
        for item in zone:
            ret[zone['ZoneId']][item] = six.text_type(zone[item])
    return ret