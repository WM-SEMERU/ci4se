def plot_cov_ellipse(cov, pos, nstd=2, **kwargs):

    def eigsorted(cov):
        vals, vecs = np.linalg.eigh(cov)
        order = vals.argsort()[::-1]
        return vals[order], vecs[:, (order)]
    vals, vecs = eigsorted(cov)
    theta = np.degrees(np.arctan2(*vecs[:, (0)][::-1]))
    width, height = 2 * nstd * np.sqrt(vals)
    ellip = Ellipse(xy=pos, width=width, height=height, angle=theta, fill=
        False, **kwargs)
    return ellip