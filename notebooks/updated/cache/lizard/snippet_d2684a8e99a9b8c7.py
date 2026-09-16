def evo_blanket(self, beta, alpha):
    evo_blanket = np.zeros(self.state_no)
    for i in range(evo_blanket.shape[0]):
        evo_blanket[i] = self.state_likelihood_markov_blanket(beta, alpha, i
            ).sum()
    if self.family_z_no > 0:
        evo_blanket = np.append([self.likelihood_markov_blanket(beta).sum()
            ] * self.family_z_no, evo_blanket)
    return evo_blanket