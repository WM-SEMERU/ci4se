def plotfft(s, fmax, doplot=False):
    fs = abs(numpy.fft.fft(s))
    f = numpy.linspace(0, fmax / 2, len(s) / 2)
    if doplot:
        plot(list(f[1:int(len(s) / 2)]), list(fs[1:int(len(s) / 2)]))
    return f[1:int(len(s) / 2)].copy(), fs[1:int(len(s) / 2)].copy()