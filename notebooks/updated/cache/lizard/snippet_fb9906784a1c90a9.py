def controlled_mc(self, sigma):
    _, Q_sigma = self.RQ_sigma(sigma)
    return MarkovChain(Q_sigma)