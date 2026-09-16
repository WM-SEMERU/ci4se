def dist_single(self, g_num, at_1, at_2):
    import numpy as np
    from scipy import linalg as spla
    from .utils import safe_cast as scast
    if not -self.num_atoms <= at_1 < self.num_atoms:
        raise IndexError("Invalid index for 'at_1' ({0})".format(at_1))
    if not -self.num_atoms <= at_2 < self.num_atoms:
        raise IndexError("Invalid index for 'at_2' ({0})".format(at_2))
    at_1 = scast(np.floor(at_1), np.int_)
    at_2 = scast(np.floor(at_2), np.int_)
    if at_1 == at_2:
        dist = 0.0
    else:
        dist = scast(spla.norm(self.displ_single(g_num, at_1, at_2)), np.float_
            )
    return dist