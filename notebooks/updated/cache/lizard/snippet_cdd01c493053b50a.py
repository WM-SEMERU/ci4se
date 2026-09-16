def calcSMAfromT(self, epsilon=0.7):
    return eq.MeanPlanetTemp(self.albedo(), self.star.T, self.star.R,
        epsilon, self.T).a