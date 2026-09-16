def _get_rule_port_ranges(rule):
    properties = rule['properties']
    if 'destinationPortRange' in properties:
        return [PortsRangeHelper._get_port_range(properties[
            'destinationPortRange'])]
    else:
        return [PortsRangeHelper._get_port_range(r) for r in properties[
            'destinationPortRanges']]