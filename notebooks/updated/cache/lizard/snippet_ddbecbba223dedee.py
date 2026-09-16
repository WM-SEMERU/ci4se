def fwhm(x, y, k=10):


    class MultiplePeaks(Exception):
        pass


    class NoPeaksFound(Exception):
        pass
    half_max = np.amax(y) / 2.0
    s = splrep(x, y - half_max)
    roots = sproot(s)
    if len(roots) > 2:
        raise MultiplePeaks(
            "The dataset appears to have multiple peaks, and thus the FWHM can't be determined."
            )
    elif len(roots) < 2:
        raise NoPeaksFound(
            'No proper peaks were found in the data set; likely the dataset is flat (e.g. all zeros).'
            )
    else:
        return roots[0], roots[1]