def d2logpdf_dlink2(self, inv_link_f, y, Y_metadata=None):
    arg = np.where(y == 1, inv_link_f, 1.0 - inv_link_f)
    ret = -1.0 / np.square(np.clip(arg, 1e-09, 1000000000.0))
    if np.any(np.isinf(ret)):
        stop
    return ret