def xtime(b, n):
    b = b.reshape(8)
    for _ in range(n):
        b = exprzeros(1) + b[:7] ^ uint2exprs(27, 8) & b[7] * 8
    return b