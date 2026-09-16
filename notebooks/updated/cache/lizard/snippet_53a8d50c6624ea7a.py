def by_location(self, location, cc=None):
    header, content = self._http_request(self.BASE_URL, location=location,
        cc=cc)
    return json.loads(content)