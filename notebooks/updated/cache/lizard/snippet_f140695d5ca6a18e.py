def _update_weight(self, data, R, n_local_subj, local_weight_offset):
    for s, subj_data in enumerate(data):
        base = s * self.prior_size
        centers = self.local_posterior_[base:base + self.K * self.n_dim
            ].reshape((self.K, self.n_dim))
        start_idx = base + self.K * self.n_dim
        end_idx = base + self.prior_size
        widths = self.local_posterior_[start_idx:end_idx].reshape((self.K, 1))
        unique_R, inds = self.get_unique_R(R[s])
        F = self.get_factors(unique_R, inds, centers, widths)
        start_idx = local_weight_offset[s]
        if s == n_local_subj - 1:
            self.local_weights_[start_idx:] = self.get_weights(subj_data, F
                ).ravel()
        else:
            end_idx = local_weight_offset[s + 1]
            self.local_weights_[start_idx:end_idx] = self.get_weights(subj_data
                , F).ravel()
    return self