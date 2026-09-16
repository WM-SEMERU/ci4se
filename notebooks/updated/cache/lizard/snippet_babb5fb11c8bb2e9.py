def update_grads(self, X, dL_dW):
    for i_seq, i_fea in enumerate(self.warping_indices):
        ai, bi = self.params[i_seq][0], self.params[i_seq][1]
        x_pow_a = np.power(self.X_normalized[:, (i_fea)], ai)
        dz_dai = bi * np.power(1 - x_pow_a, bi - 1) * x_pow_a * np.log(self
            .X_normalized[:, (i_fea)])
        dz_dbi = -np.power(1 - x_pow_a, bi) * np.log(1 - x_pow_a)
        dL_dai = np.sum(dL_dW[:, (i_fea)] * dz_dai)
        dL_dbi = np.sum(dL_dW[:, (i_fea)] * dz_dbi)
        self.params[i_seq][0].gradient[:] = dL_dai
        self.params[i_seq][1].gradient[:] = dL_dbi