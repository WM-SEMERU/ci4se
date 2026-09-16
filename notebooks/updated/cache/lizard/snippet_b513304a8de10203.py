def mse(vref, vcmp):
    r = np.asarray(vref, dtype=np.float64).ravel()
    c = np.asarray(vcmp, dtype=np.float64).ravel()
    return np.mean(np.abs(r - c) ** 2)