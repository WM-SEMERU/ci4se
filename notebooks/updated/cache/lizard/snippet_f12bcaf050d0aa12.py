def _make_request(self, suburl):
    url = '{}/{}'.format(self.API_BASE_URL, suburl)
    response = self.session.get(url)
    response.raise_for_status()
    return response.json()