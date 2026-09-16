def get(self, url):
    return requests.get(url, params=self.data, headers=self.config.HEADERS)