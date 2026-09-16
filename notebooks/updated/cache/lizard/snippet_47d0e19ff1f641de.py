def bck_from_spt(spt):
    spt = np.asfarray(spt)
    return np.piecewise(spt, [spt < 30, spt < 19, spt <= 14, spt < 10, (spt <
        2) | (spt >= 30)], [lambda s: 3.41 - 0.21 * (s - 20), lambda s: 
        3.42 - 0.075 * (s - 14), lambda s: 3.42 + 0.075 * (s - 14), lambda
        s: 2.43 + 0.0895 * s, np.nan])