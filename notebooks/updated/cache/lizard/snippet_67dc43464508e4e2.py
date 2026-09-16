def get(self, name):
    import requests
    url = urljoin(self.base_url, name)
    response = requests.get(url)
    return response.content