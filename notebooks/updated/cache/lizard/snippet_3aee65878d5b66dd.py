def reverse_delete_ipv6(self, subid, ipaddr, params=None):
    params = update_params(params, {'SUBID': subid, 'ip': ipaddr})
    return self.request('/v1/server/reverse_delete_ipv6', params, 'POST')