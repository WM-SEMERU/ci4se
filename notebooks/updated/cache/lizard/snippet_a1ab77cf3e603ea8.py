def get_vpn(self, vpn_name):
    request_url = self._build_url(['VPN', vpn_name])
    return self._do_request('GET', request_url)