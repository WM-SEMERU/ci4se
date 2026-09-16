def zcross(seq, hysteresis=0, first_sign=0):
    neg_hyst = -hysteresis
    seq_iter = iter(seq)
    if first_sign == 0:
        last_sign = 0
        for el in seq_iter:
            yield 0
            if el > hysteresis or el < neg_hyst:
                last_sign = -1 if el < 0 else 1
                break
    else:
        last_sign = -1 if first_sign < 0 else 1
    for el in seq_iter:
        if el * last_sign < neg_hyst:
            last_sign = -1 if el < 0 else 1
            yield 1
        else:
            yield 0