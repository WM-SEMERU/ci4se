def fourier(x, N):
    term = 0.0
    for n in range(1, N, 2):
        term += 1.0 / n * math.sin(n * math.pi * x / L)
    return 4.0 / math.pi * term