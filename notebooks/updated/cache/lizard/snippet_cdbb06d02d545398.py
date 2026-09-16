def add(self):
    yield self.client.create(self.path)
    yield self.client.create(self.path + '/type', self.name)
    yield self.client.create(self.path + '/state')
    yield self.client.create(self.path + '/machines', '[]')
    log.debug("registered service '%s' at %s." % (self.name, self.path))