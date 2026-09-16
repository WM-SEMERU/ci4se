def _pruning(self, X, y_true, cost_mat):
    nodes = self._nodes(self.tree_.tree_pruned)
    n_nodes = len(nodes)
    gains = np.zeros(n_nodes)
    y_pred = self._classify(X, self.tree_.tree_pruned)
    cost_base = cost_loss(y_true, y_pred, cost_mat)
    for m, node in enumerate(nodes):
        temp_tree = self._delete_node(self.tree_.tree_pruned, node)
        y_pred = self._classify(X, temp_tree)
        nodes_pruned = self._nodes(temp_tree)
        gain = (cost_base - cost_loss(y_true, y_pred, cost_mat)) / cost_base
        gain_size = (len(nodes) - len(nodes_pruned)) * 1.0 / len(nodes)
        gains[m] = gain * gain_size
    best_gain = np.max(gains)
    best_node = nodes[int(np.argmax(gains))]
    if best_gain > self.min_gain:
        self.tree_.tree_pruned = self._delete_node(self.tree_.tree_pruned,
            best_node)
        if best_node != 0:
            self._pruning(X, y_true, cost_mat)