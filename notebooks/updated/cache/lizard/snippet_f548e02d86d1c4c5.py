def edit_secondary_name_server(self, zone_name, primary=None, backup=None,
    second_backup=None):
    name_server_info = {}
    if primary is not None:
        name_server_info['nameServerIp1'] = {'ip': primary}
    if backup is not None:
        name_server_info['nameServerIp2'] = {'ip': backup}
    if second_backup is not None:
        name_server_info['nameServerIp3'] = {'ip': second_backup}
    name_server_ip_list = {'nameServerIpList': name_server_info}
    secondary_zone_info = {'primaryNameServers': name_server_ip_list}
    zone_data = {'secondaryCreateInfo': secondary_zone_info}
    return self.rest_api_connection.patch('/v1/zones/' + zone_name, json.
        dumps(zone_data))