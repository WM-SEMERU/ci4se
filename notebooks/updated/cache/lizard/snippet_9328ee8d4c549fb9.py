def klm(p, q):
    p, q = flatten(p), flatten(q)
    return max(abs(p * np.nan_to_num(np.log(p / q))))