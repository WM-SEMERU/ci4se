def unassign_floating_ip(self, ip_addr):
    if self.api_version == 2:
        params = {'type': 'unassign'}
        json = self.request('/floating_ips/' + ip_addr + '/actions', params
            =params, method='POST')
        return json['action']
    else:
        raise DoError(v2_api_required_str)