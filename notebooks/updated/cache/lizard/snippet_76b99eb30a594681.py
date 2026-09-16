def delete(self, action, headers=None):
    return self.request(make_url(self.endpoint, action), method='DELETE',
        headers=headers)