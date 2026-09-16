def min_or(a, b, c, d, w):
    m = 1 << w - 1
    while m != 0:
        if ~a & c & m != 0:
            temp = (a | m) & -m
            if temp <= b:
                a = temp
                break
        elif a & ~c & m != 0:
            temp = (c | m) & -m
            if temp <= d:
                c = temp
                break
        m >>= 1
    return a | c