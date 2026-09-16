def _psi(self, m):
    if self.twominusalpha == 0.0:
        return -2.0 * self.a ** 2 * (self.a / m
            ) ** self.betaminusalpha / self.betaminusalpha * special.hyp2f1(
            self.betaminusalpha, self.betaminusalpha, self.betaminusalpha +
            1, -self.a / m)
    else:
        return -2.0 * self.a ** 2 * (self.psi_inf - (m / self.a) ** self.
            twominusalpha / self.twominusalpha * special.hyp2f1(self.
            twominusalpha, self.betaminusalpha, self.threeminusalpha, -m /
            self.a))