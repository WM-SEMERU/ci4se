def _get_equivalent_distances_east(wid, lng, mag, repi, focal_depth=10.0,
    ab06=False):
    dtop = focal_depth - 0.5 * wid
    if ab06:
        ztor_ab06 = 21 - 2.5 * mag
        dtop = np.max([ztor_ab06, dtop])
    ztor = max(0, dtop)
    dsurf = np.max([repi - 0.3 * lng, 0.1 * np.ones_like(repi)], axis=0)
    rrup = (dsurf ** 2 + ztor ** 2) ** 0.5
    return dsurf, rrup