def energy(self):
    r
    s, b, W, N = self.state, self.b, self.W, self.N
    self.E = -sum(s * b) - sum([(s[i] * s[j] * W[i, j]) for i, j in product
        (range(N), range(N)) if i < j])
    self.low_energies[-1] = self.E
    self.low_energies.sort()
    self.high_energies[-1] = self.E
    self.high_energies.sort()
    self.high_energies = self.high_energies[::-1]
    return self.E