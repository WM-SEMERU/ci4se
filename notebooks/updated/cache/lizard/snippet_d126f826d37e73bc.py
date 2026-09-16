def signed_mult(a, b):
    a, b = as_wires(a), as_wires(b)
    final_len = len(a) + len(b)
    a, b = a.sign_extended(final_len), b.sign_extended(final_len)
    return (a * b)[0:final_len]