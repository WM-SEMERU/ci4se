def make_rsa_keys(bits=2048, e=65537, k=64):
    p, q = None, None
    while p == q:
        p, q = get_prime(bits // 2), get_prime(bits // 2)
    n = p * q
    phi_n = phi(n, p, q)
    d = mult_inv(e, phi_n)
    return n, e, d