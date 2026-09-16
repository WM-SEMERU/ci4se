def generate_matches(self, nodes):
    r = {}
    if nodes and self.match(nodes[0], r):
        yield 1, r