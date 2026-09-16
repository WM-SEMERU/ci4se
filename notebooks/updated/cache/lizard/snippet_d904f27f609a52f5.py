def concatenate_slh(self, other):
    selfS = self.S
    otherS = other.S
    new_S = block_matrix(selfS, zerosm((selfS.shape[0], otherS.shape[1]),
        dtype=int), zerosm((otherS.shape[0], selfS.shape[1]), dtype=int),
        otherS)
    new_L = vstackm((self.L, other.L))
    new_H = self.H + other.H
    return SLH(new_S, new_L, new_H)