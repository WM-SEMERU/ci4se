def signed_add(a, b):
    a, b = match_bitwidth(as_wires(a), as_wires(b), signed=True)
    result_len = len(a) + 1
    ext_a = a.sign_extended(result_len)
    ext_b = b.sign_extended(result_len)
    return (ext_a + ext_b)[0:result_len]