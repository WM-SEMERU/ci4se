def begin(self):
    self.url = self.server.wiki.create(self)
    if not self.testmode:
        self.commit.create_status('pending', self.url, 'Running unit tests...')