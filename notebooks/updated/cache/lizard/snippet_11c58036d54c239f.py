def commutator(A, B=None):
    if B:
        return A * B - B * A
    return SPre(A) - SPost(A)