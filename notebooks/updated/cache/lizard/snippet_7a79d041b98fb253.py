def load_spectrum(path, smoothing=181, DF=-8.0):
    try:
        ang, lflam = np.loadtxt(path, usecols=(0, 1)).T
    except ValueError:
        with open(path, 'rb') as f:

            def lines():
                for line in f:
                    yield line.replace(b'D', b'e')
            ang, lflam = np.genfromtxt(lines(), delimiter=(13, 12)).T
    z = ang.argsort()
    ang = ang[z]
    flam = 10 ** (lflam[z] + DF)
    del z
    if smoothing is not None:
        if isinstance(smoothing, int):
            smoothing = np.hamming(smoothing)
        else:
            smoothing = np.asarray(smoothing)
        wnorm = np.convolve(np.ones_like(smoothing), smoothing, mode='valid')
        smoothing = smoothing / wnorm
        smooth = lambda a: np.convolve(a, smoothing, mode='valid')[::
            smoothing.size]
        ang = smooth(ang)
        flam = smooth(flam)
    return pd.DataFrame({'wlen': ang, 'flam': flam})