def download(self):
    if self.url:
        try:
            return requests.get(self.url).content
        except requests.RequestException as e:
            raise GyazoError(str(e))
    return None