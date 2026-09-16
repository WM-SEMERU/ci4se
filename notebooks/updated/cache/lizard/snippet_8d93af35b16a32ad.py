def uncompress(pub):
    yp = int(pub[:2], 16) - 2
    x = int(pub[2:], 16)
    a = (pow_mod(x, 3, P) + 7) % P
    y = pow_mod(a, (P + 1) // 4, P)
    if y % 2 != yp:
        y = -y % P
    x = dechex(x, 32)
    y = dechex(y, 32)
    return '04' + x + y