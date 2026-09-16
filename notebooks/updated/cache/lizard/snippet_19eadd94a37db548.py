def fpbspl(t, n, k, x, l, h, hh):
    h[0] = 1.0
    for j in range(1, k + 1):
        hh[0:j] = h[0:j]
        h[0] = 0.0
        for i in range(j):
            li = l + i
            f = hh[i] / (t[li] - t[li - j])
            h[i] = h[i] + f * (t[li] - x)
            h[i + 1] = f * (x - t[li - j])