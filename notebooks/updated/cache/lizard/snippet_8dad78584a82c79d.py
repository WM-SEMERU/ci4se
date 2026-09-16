def _requestDetails(self, ip_address=None):
    if ip_address not in self.cache:
        url = self.API_URL
        if ip_address:
            url += '/' + ip_address
        response = requests.get(url, headers=self._get_headers(), **self.
            request_options)
        if response.status_code == 429:
            raise RequestQuotaExceededError()
        response.raise_for_status()
        self.cache[ip_address] = response.json()
    return self.cache[ip_address]