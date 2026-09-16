def predict_wishart_embedding(self, Xnew, kern=None, mean=True, covariance=True
    ):
    if kern is None:
        kern = self.kern
    mu_jac, var_jac = self.predict_jacobian(Xnew, kern, full_cov=False)
    mumuT = np.einsum('iqd,ipd->iqp', mu_jac, mu_jac)
    Sigma = np.zeros(mumuT.shape)
    if var_jac.ndim == 4:
        Sigma = var_jac.sum(-1)
    else:
        Sigma = self.output_dim * var_jac
    G = 0.0
    if mean:
        G += mumuT
    if covariance:
        G += Sigma
    return G