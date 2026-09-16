def _single_projector_generator(ket_op, bra_op, index):
    if not isinstance(ket_op, int):
        raise TypeError('ket_op needs to be an integer')
    if not isinstance(bra_op, int):
        raise TypeError('ket_op needs to be an integer')
    if ket_op not in [0, 1] or bra_op not in [0, 1]:
        raise ValueError('bra and ket op needs to be either 0 or 1')
    if ket_op == 0 and bra_op == 0:
        return 0.5 * (sZ(index) + sI(index))
    elif ket_op == 0 and bra_op == 1:
        return 0.5 * (sX(index) + 1.0j * sY(index))
    elif ket_op == 1 and bra_op == 0:
        return 0.5 * (sX(index) - 1.0j * sY(index))
    else:
        return 0.5 * (sI(index) - sZ(index))