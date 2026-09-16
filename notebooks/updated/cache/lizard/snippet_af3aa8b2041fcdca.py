def serialize(pca, **kwargs):
    strike, dip, rake = pca.strike_dip_rake()
    hyp_axes = sampling_axes(pca)
    return dict(**kwargs, principal_axes=pca.axes.tolist(), hyperbolic_axes
        =hyp_axes.tolist(), n_samples=pca.n, strike=strike, dip=dip, rake=
        rake, angular_errors=[(2 * N.degrees(i)) for i in angular_errors(
        hyp_axes)])