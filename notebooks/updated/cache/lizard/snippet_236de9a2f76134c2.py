def scale_stoichiometry(self, scaling):
    return {k: (v * scaling) for k, v in self.stoichiometry.items()}