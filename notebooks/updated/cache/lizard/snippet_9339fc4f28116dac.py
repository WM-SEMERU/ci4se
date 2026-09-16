def recurring(self, offset=0, count=25):
    return self.client('jobs', 'recurring', self.name, offset, count)