def labels(self):
    return {j: ('x= ' + str(round(x, 4)) + ' energy in eV/atom = ' + str(
        round(energy, 4)) + ' ' + str(reaction)) for j, x, energy, reaction,
        _ in self.get_kinks()}