def get_lats_from_cartesian(x__, y__, z__, thr=0.8):
    lats = np.where(np.logical_and(np.less(z__, thr * EARTH_RADIUS), np.
        greater(z__, -1.0 * thr * EARTH_RADIUS)), 90 - rad2deg(arccos(z__ /
        EARTH_RADIUS)), sign(z__) * (90 - rad2deg(arcsin(sqrt(x__ ** 2 + 
        y__ ** 2) / EARTH_RADIUS))))
    return lats