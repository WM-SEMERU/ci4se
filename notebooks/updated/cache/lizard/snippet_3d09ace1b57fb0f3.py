def _simulate_coef_from_bootstraps(self, n_draws, coef_bootstraps,
    cov_bootstraps):
    random_bootstrap_indices = np.random.choice(np.arange(len(
        coef_bootstraps)), size=n_draws, replace=True)
    bootstrap_index_to_draw_indices = defaultdict(list)
    for draw_index, bootstrap_index in enumerate(random_bootstrap_indices):
        bootstrap_index_to_draw_indices[bootstrap_index].append(draw_index)
    coef_draws = np.empty((n_draws, len(self.coef_)))
    for bootstrap, draw_indices in bootstrap_index_to_draw_indices.items():
        coef_draws[draw_indices] = np.random.multivariate_normal(
            coef_bootstraps[bootstrap], cov_bootstraps[bootstrap], size=len
            (draw_indices))
    return coef_draws