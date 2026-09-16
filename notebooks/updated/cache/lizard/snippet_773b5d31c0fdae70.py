def solve_dp(self, lam):
    cur_converge = self.converge + 1
    step = 0
    self.solve_gfl(lam)
    beta2 = np.copy(self.beta)
    while cur_converge > self.converge and step < self.max_dp_steps:
        u = lam / (1 + np.abs(self.beta[self.trails[::2]] - self.beta[self.
            trails[1::2]]))
        temp = self.beta
        self.beta = beta2
        beta2 = temp
        self.solve_gfl(u)
        cur_converge = np.sqrt(((self.beta - beta2) ** 2).sum())
        step += 1
    self.steps.append(step)
    return self.beta