def sparse_hessian_log_joint(self, x):
    T, D = self.T, self.D_latent
    assert x.shape == (T, D)
    J_diag, J_upper_diag = self.sparse_J_prior
    H_diag, H_upper_diag = -J_diag, -J_upper_diag
    H_diag += self.hessian_local_log_likelihood(x)
    H_diag -= 1e-08 * np.eye(D)
    return H_diag, H_upper_diag