def _process_with_joblib(self, X: Union[pd.DataFrame, np.ndarray], n_refs:
    int, cluster_array: np.ndarray):
    if Parallel is None:
        raise EnvironmentError(
            'joblib is not installed; cannot use joblib as the parallel backend!'
            )
    with Parallel(n_jobs=self.n_jobs) as parallel:
        for gap_value, n_clusters in parallel(delayed(self._calculate_gap)(
            X, n_refs, n_clusters) for n_clusters in cluster_array):
            yield gap_value, n_clusters