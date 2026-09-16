def get_kx(N, dx):
    L = N * dx
    odd = N & 1 and True or False
    k = ft.fftfreq(N, d=dx)
    imx = (N - 1) / 2 if odd else N / 2
    return k, L, imx