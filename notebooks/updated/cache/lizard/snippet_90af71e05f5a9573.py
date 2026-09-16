def mass_fraction_within_radius(self, kwargs_lens, center_x, center_y,
    theta_E, numPix=100):
    x_grid, y_grid = util.make_grid(numPix=numPix, deltapix=2.0 * theta_E /
        numPix)
    x_grid += center_x
    y_grid += center_y
    mask = mask_util.mask_sphere(x_grid, y_grid, center_x, center_y, theta_E)
    kappa_list = []
    for i in range(len(kwargs_lens)):
        kappa = self.LensModel.kappa(x_grid, y_grid, kwargs_lens, k=i)
        kappa_mean = np.sum(kappa * mask) / np.sum(mask)
        kappa_list.append(kappa_mean)
    return kappa_list