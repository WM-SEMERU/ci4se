def calc_complex(mag, pha):
    complx = [(10 ** m * math.e ** (1.0j * p / 1000.0)) for m, p in zip(mag,
        pha)]
    real = [math.log10((1 / c).real) for c in complx]
    imag = []
    for c in complx:
        if (1 / c).imag == 0:
            imag.append(math.nan)
        else:
            i = math.log10(abs((1 / c).imag))
            imag.append(i)
    return real, imag