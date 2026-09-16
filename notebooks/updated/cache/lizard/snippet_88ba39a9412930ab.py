def connect_network_gateway(self, gateway_id, body=None):
    base_uri = self.network_gateway_path % gateway_id
    return self.put('%s/connect_network' % base_uri, body=body)