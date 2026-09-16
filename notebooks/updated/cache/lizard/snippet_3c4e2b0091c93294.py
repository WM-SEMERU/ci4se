def get_comments(self):
    url = self._imgur._base_url + '/3/gallery/{0}/comments'.format(self.id)
    resp = self._imgur._send_request(url)
    return [Comment(com, self._imgur) for com in resp]