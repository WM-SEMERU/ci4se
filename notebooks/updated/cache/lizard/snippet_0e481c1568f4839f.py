def nfwAlpha(self, R, Rs, rho0, r_trunc, ax_x, ax_y):
    if isinstance(R, int) or isinstance(R, float):
        R = max(R, 1e-05)
    else:
        R[R <= 1e-05] = 1e-05
    x = R / Rs
    tau = float(r_trunc) / Rs
    gx = self._g(x, tau)
    a = 4 * rho0 * Rs * gx / x ** 2
    return a * ax_x, a * ax_y