def sym_log_map(cls, q, p):
    inv_sqrt_q = q ** -0.5
    return Quaternion.log(inv_sqrt_q * p * inv_sqrt_q)