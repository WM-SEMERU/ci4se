def get_snmp_information(self):
    snmp_dict = {'chassis_id': 'unknown', 'community': {}, 'contact':
        'unknown', 'location': 'unknown'}
    command = 'show run | include snmp-server'
    output = self._send_command(command)
    for line in output.splitlines():
        fields = line.split()
        if 'snmp-server community' in line:
            name = fields[2]
            if 'community' not in snmp_dict.keys():
                snmp_dict.update({'community': {}})
            snmp_dict['community'].update({name: {}})
            try:
                snmp_dict['community'][name].update({'mode': fields[3].lower()}
                    )
            except IndexError:
                snmp_dict['community'][name].update({'mode': 'N/A'})
            try:
                snmp_dict['community'][name].update({'acl': fields[4]})
            except IndexError:
                snmp_dict['community'][name].update({'acl': 'N/A'})
        elif 'snmp-server location' in line:
            snmp_dict['location'] = ' '.join(fields[2:])
        elif 'snmp-server contact' in line:
            snmp_dict['contact'] = ' '.join(fields[2:])
        elif 'snmp-server chassis-id' in line:
            snmp_dict['chassis_id'] = ' '.join(fields[2:])
    if snmp_dict['chassis_id'] == 'unknown':
        command = 'show snmp chassis'
        snmp_chassis = self._send_command(command)
        snmp_dict['chassis_id'] = snmp_chassis
    return snmp_dict