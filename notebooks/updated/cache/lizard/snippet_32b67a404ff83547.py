def get_tunnel(self, tunnel_id):
    method = 'GET'
    endpoint = '/rest/v1/{}/tunnels/{}'.format(self.client.sauce_username,
        tunnel_id)
    return self.client.request(method, endpoint)