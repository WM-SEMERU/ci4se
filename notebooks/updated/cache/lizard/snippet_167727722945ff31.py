def update_DOM(self):
    response = self.fetch()
    self._DOM = html.fromstring(response.text)
    return self