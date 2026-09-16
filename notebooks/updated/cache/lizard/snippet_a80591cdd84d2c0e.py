def get_concurrency(self):
    method = 'GET'
    endpoint = '/rest/v1.1/users/{}/concurrency'.format(self.client.
        sauce_username)
    return self.client.request(method, endpoint)