def map_frames(self, old_indices):
    nfeatures = len(old_indices)
    noldfeatures = len(self.state_vec)
    if nfeatures > 0:
        self.state_vec = self.state_vec[old_indices]
        self.state_cov = self.state_cov[old_indices]
        self.noise_var = self.noise_var[old_indices]
        if self.has_cached_obs_vec:
            self.obs_vec = self.obs_vec[old_indices]
        if self.has_cached_predicted_state_vec:
            self.p_state_vec = self.p_state_vec[old_indices]
        if len(self.state_noise_idx) > 0:
            reverse_indices = -np.ones(noldfeatures, int)
            reverse_indices[old_indices] = np.arange(nfeatures)
            self.state_noise_idx = reverse_indices[self.state_noise_idx]
            self.state_noise = self.state_noise[(self.state_noise_idx != -1), :
                ]
            self.state_noise_idx = self.state_noise_idx[self.
                state_noise_idx != -1]