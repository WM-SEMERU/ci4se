def isochone_ratio(e, rd, r_hyp):
    if e == 0.0:
        c_prime = 0.8
    elif e > 0.0:
        c_prime = 1.0 / (1.0 / 0.8 - (r_hyp - rd) / e)
    return c_prime