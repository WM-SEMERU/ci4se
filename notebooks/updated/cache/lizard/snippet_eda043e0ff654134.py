def prime_ge(n):
    p = max(np.ceil(n), 2)
    while not is_prime(p):
        p += 1
    return p