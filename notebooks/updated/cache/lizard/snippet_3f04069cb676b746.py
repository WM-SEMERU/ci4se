def _compute_acq_withGradients(self, x):
    fmin = self.model.get_fmin()
    m, s, dmdx, dsdx = self.model.predict_withGradients(x)
    phi, Phi, u = get_quantiles(self.jitter, fmin, m, s)
    f_acqu = s * (u * Phi + phi)
    df_acqu = dsdx * phi - Phi * dmdx
    return f_acqu, df_acqu