def Imm(extended_map, s, lmax):
    import numpy as np
    extended_map = np.ascontiguousarray(extended_map, dtype=np.complex128)
    NImm = (2 * lmax + 1) ** 2
    imm = np.empty(NImm, dtype=np.complex128)
    _Imm(extended_map, imm, s, lmax)
    return imm