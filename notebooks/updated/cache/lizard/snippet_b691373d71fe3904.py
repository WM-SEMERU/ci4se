def getNextSample(self, V):
    phi = self.phi
    wmg = self.wmg
    W = []
    W.append(V[0])
    for j in range(2, len(V) + 1):
        randomSelect = random.random()
        threshold = 0.0
        denom = 1.0
        for k in range(1, j):
            denom = denom + phi ** k
        for k in range(1, j + 1):
            numerator = phi ** (j - k)
            threshold = threshold + numerator / denom
            if randomSelect <= threshold:
                W.insert(k - 1, V[j - 1])
                break
    acceptanceRatio = self.calcAcceptanceRatio(V, W)
    prob = min(1.0, acceptanceRatio)
    if random.random() <= prob:
        V = W
    return V