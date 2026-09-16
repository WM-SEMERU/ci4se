def confirm_vlan(self, number_net, id_environment_vlan, ip_version=None):
    url = 'vlan/confirm/' + str(number_net
        ) + '/' + id_environment_vlan + '/' + str(ip_version)
    code, xml = self.submit(None, 'GET', url)
    return self.response(code, xml)