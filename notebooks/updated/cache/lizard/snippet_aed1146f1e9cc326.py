def get_network_ipv6(self, id_network):
    if not is_valid_int_param(id_network):
        raise InvalidParameterError(
            'O id do rede ip6 foi informado incorretamente.')
    url = 'network/ipv6/id/' + str(id_network) + '/'
    code, xml = self.submit(None, 'GET', url)
    return self.response(code, xml)