def assign_floating_ip(self, ip_addr, droplet_id):
    if self.api_version == 2:
        params = {'type': 'assign', 'droplet_id': droplet_id}
        json = self.request('/floating_ips/' + ip_addr + '/actions', params
            =params, method='POST')
        return json['action']
    else:
        raise DoError(v2_api_required_str)