def get_server_by_ip(self, ip_address):
    data = self.get_request('/ip_address/{0}'.format(ip_address))
    UUID = data['ip_address']['server']
    return self.get_server(UUID)