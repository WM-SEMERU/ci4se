def xyz_with_ports(self):
    if not self.children:
        pos = self._pos
    else:
        arr = np.fromiter(itertools.chain.from_iterable(particle.pos for
            particle in self.particles(include_ports=True)), dtype=float)
        pos = arr.reshape((-1, 3))
    return pos