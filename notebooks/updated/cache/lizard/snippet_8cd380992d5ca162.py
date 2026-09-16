def fit(self, X, y=None, input_type='affinity'):
    X = self._validate_input(X, input_type)
    self.fit_geometry(X, input_type)
    random_state = check_random_state(self.random_state)
    self.embedding_, self.eigen_vectors_, self.P_ = spectral_clustering(self
        .geom_, K=self.K, eigen_solver=self.eigen_solver, random_state=self
        .random_state, solver_kwds=self.solver_kwds, renormalize=self.
        renormalize, stabalize=self.stabalize, additional_vectors=self.
        additional_vectors)