def walk(self, cli):
    yield self
    for c in self.children:
        for i in c.walk(cli):
            yield i