def energy_at_conditions(self, pH, V):
    return self.energy + self.npH * PREFAC * pH + self.nPhi * V