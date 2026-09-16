def get_tunnels(self):
    method = 'GET'
    endpoint = '/rest/v1/{}/tunnels'.format(self.client.sauce_username)
    return self.client.request(method, endpoint)