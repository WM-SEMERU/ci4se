def server_lia_countries(self):
    response = self._post(self.apiurl + '/v2/server/lia_countries', data={
        'apikey': self.apikey})
    return self._raise_or_extract(response)