def square_root_mod_prime(a, p):
    assert 0 <= a < p
    assert 1 < p
    if a == 0:
        return 0
    if p == 2:
        return a
    jac = jacobi(a, p)
    if jac == -1:
        raise SquareRootError('%d has no square root modulo %d' % (a, p))
    if p % 4 == 3:
        return modular_exp(a, (p + 1) // 4, p)
    if p % 8 == 5:
        d = modular_exp(a, (p - 1) // 4, p)
        if d == 1:
            return modular_exp(a, (p + 3) // 8, p)
        if d == p - 1:
            return 2 * a * modular_exp(4 * a, (p - 5) // 8, p) % p
        raise RuntimeError("Shouldn't get here.")
    for b in range(2, p):
        if jacobi(b * b - 4 * a, p) == -1:
            f = a, -b, 1
            ff = polynomial_exp_mod((0, 1), (p + 1) // 2, f, p)
            assert ff[1] == 0
            return ff[0]
    raise RuntimeError('No b found.')