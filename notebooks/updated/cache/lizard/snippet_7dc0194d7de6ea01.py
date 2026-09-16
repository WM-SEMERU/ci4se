def tukey(winlen, alpha):
    taper = hann(winlen * alpha)
    rect = np.ones(winlen - len(taper) + 1)
    win = fftconvolve(taper, rect)
    win = win / np.amax(win)
    return win