def surrounding_nodes(self, position):
    n_node_index, n_node_position, n_node_error = self.nearest_node(position)
    if n_node_error == 0.0:
        index_mod = []
        for i in range(len(n_node_index)):
            new_point = np.asarray(n_node_position)
            new_point[i] += 1e-05 * np.abs(new_point[i])
            try:
                self.nearest_node(tuple(new_point))
                index_mod.append(-1)
            except ValueError:
                index_mod.append(1)
    else:
        index_mod = []
        for i in range(len(n_node_index)):
            if n_node_position[i] > position[i]:
                index_mod.append(-1)
            else:
                index_mod.append(1)
    return tuple(n_node_index), tuple(index_mod)