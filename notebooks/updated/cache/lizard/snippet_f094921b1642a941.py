def xyz(self):
    if not self.children:
        pos = np.expand_dims(self._pos, axis=0)
    else:
        arr = np.fromiter(itertools.chain.from_iterable(particle.pos for
            particle in self.particles()), dtype=float)
        pos = arr.reshape((-1, 3))
    return pos