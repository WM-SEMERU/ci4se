def plot_prior_dates(self, dwidth=30, ax=None):
    if ax is None:
        ax = plt.gca()
    depth, probs = self.prior_dates()
    pat = []
    for i, d in enumerate(depth):
        p = probs[i]
        z = np.array([p[:, (0)], dwidth * p[:, (1)] / np.sum(p[:, (1)])])
        z = z[:, (z[0].argsort(kind='mergesort'))]
        zy = np.linspace(np.min(z[0]), np.max(z[0]), num=200)
        zp = np.interp(x=zy, xp=z[0], fp=z[1])
        pol = np.vstack([np.concatenate([d + zp, d - zp[::-1]]), np.
            concatenate([zy, zy[::-1]])])
        pat.append(Polygon(pol.T))
    p = PatchCollection(pat)
    p.set_label('Prior dates')
    ax.add_collection(p)
    ax.autoscale_view()
    ax.set_ylabel('Age (cal yr BP)')
    ax.set_xlabel('Depth (cm)')
    ax.grid(True)
    return ax