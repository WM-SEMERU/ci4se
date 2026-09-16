def fit(self, index, n_nodes, tau_matrix, previous_tree, edges=None):
    self.level = index + 1
    self.n_nodes = n_nodes
    self.tau_matrix = tau_matrix
    self.previous_tree = previous_tree
    self.edges = edges or []
    if not self.edges:
        if self.level == 1:
            self.u_matrix = previous_tree
            self._build_first_tree()
        else:
            self._build_kth_tree()
        self.prepare_next_tree()
    self.fitted = True