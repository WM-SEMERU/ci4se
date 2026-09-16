def naive_peaks(vec, k=33):
    a = smooth_hanning(vec, k)
    k2 = (k - 1) / 2
    peaks = np.r_[True, a[1:] > a[:-1]] & np.r_[a[:-1] > a[1:], True]
    p = np.array(np.where(peaks)[0])
    maxidx = np.zeros(np.shape(p))
    maxvals = np.zeros(np.shape(p))
    for i, pk in enumerate(p):
        maxidx[i] = np.argmax(vec[pk - k2:pk + k2]) + pk - k2
        maxvals[i] = np.max(vec[pk - k2:pk + k2])
    out = np.array([maxidx, maxvals]).T
    return out[(-out[:, (1)]).argsort()]