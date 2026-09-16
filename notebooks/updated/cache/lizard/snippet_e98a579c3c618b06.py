def add_snmp(data, interfaces):
    snmp_interface = []
    if interfaces:
        interfaces = map(str, interfaces)
        for interface in data:
            interface_id = str(interface.get('interface_id'))
            for if_def in interface.get('interfaces', []):
                _interface_id = None
                if 'vlan_id' in if_def:
                    _interface_id = '{}.{}'.format(interface_id, if_def[
                        'vlan_id'])
                else:
                    _interface_id = interface_id
                if _interface_id in interfaces and 'type' not in interface:
                    for node in if_def.get('nodes', []):
                        snmp_interface.append({'address': node.get(
                            'address'), 'nicid': _interface_id})
    return snmp_interface