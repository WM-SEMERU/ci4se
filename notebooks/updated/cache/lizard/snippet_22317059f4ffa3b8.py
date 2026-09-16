def basis_state(i, n):
    v = sympy.zeros(n, 1)
    v[i] = 1
    return v