def scan(self, ids=range(254)):
    return [id for id in ids if self.ping(id)]