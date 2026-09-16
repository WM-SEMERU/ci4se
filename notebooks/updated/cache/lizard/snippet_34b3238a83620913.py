def create_secondary_zone(self, account_name, zone_name, master, tsig_key=
    None, key_value=None):
    zone_properties = {'name': zone_name, 'accountName': account_name,
        'type': 'SECONDARY'}
    if tsig_key is not None and key_value is not None:
        name_server_info = {'ip': master, 'tsigKey': tsig_key,
            'tsigKeyValue': key_value}
    else:
        name_server_info = {'ip': master}
    name_server_ip_1 = {'nameServerIp1': name_server_info}
    name_server_ip_list = {'nameServerIpList': name_server_ip_1}
    secondary_zone_info = {'primaryNameServers': name_server_ip_list}
    zone_data = {'properties': zone_properties, 'secondaryCreateInfo':
        secondary_zone_info}
    return self.rest_api_connection.post('/v1/zones', json.dumps(zone_data))