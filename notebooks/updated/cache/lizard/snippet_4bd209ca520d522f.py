def fundamental_frequency(s, FS):
    s = s - mean(s)
    f, fs = plotfft(s, FS, doplot=False)
    fs = fs[1:int(len(fs) / 2)]
    f = f[1:int(len(f) / 2)]
    cond = find(f > 0.5)[0]
    bp = bigPeaks(fs[cond:], 0)
    if bp == []:
        f0 = 0
    else:
        bp = bp + cond
        f0 = f[min(bp)]
    return f0