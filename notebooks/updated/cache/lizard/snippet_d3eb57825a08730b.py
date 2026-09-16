def phi(self):
    sum = 0.0
    for grp, contrib in self.phi_components.items():
        sum += contrib
    return sum