def spawn_generator(self, g):
    try:
        return self.mapping[g]
    except KeyError:
        return g._spawn(self)