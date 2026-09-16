def b1_boundary(b_hi, N):
    b_lo = b_hi - 1
    b1_lo = b1_theory(N, b_to_mu(b_lo))
    b1_hi = b1_theory(N, b_to_mu(b_hi))
    if b1_lo >= -4:
        return np.sqrt(b1_lo * b1_hi)
    else:
        return 0.5 * (b1_lo + b1_hi)