def list(self):
    response = self.session.get(self.url)
    return [Bot(self, **bot) for bot in response.data]