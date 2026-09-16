def triangle_unaddress(fx, tr):
    fx = np.asarray(fx)
    tr = np.asarray(tr)
    ab = fx[1] - fx[0]
    ac = fx[2] - fx[0]
    bc = fx[2] - fx[1]
    return np.asarray([(ax + tr[1] * (abx + tr[0] * bcx)) for ax, bcx, abx in
        zip(fx[0], bc, ab)])