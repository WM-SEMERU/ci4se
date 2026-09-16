def _build_A(self, force=False):
    r
    if force:
        self._pure_A = None
    if self._pure_A is None:
        network = self.project.network
        phase = self.project.phases()[self.settings['phase']]
        g = phase[self.settings['conductance']]
        am = network.create_adjacency_matrix(weights=g, fmt='coo')
        self._pure_A = spgr.laplacian(am)
    self.A = self._pure_A.copy()