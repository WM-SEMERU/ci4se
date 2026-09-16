def find_train_knns(self, data_activations):
    knns_ind = {}
    knns_labels = {}
    for layer in self.layers:
        data_activations_layer = copy.copy(data_activations[layer])
        nb_data = data_activations_layer.shape[0]
        data_activations_layer /= np.linalg.norm(data_activations_layer, axis=1
            ).reshape(-1, 1)
        data_activations_layer -= self.centers[layer]
        knns_ind[layer] = np.zeros((data_activations_layer.shape[0], self.
            neighbors), dtype=np.int32)
        knn_errors = 0
        for i in range(data_activations_layer.shape[0]):
            query_res = self.query_objects[layer].find_k_nearest_neighbors(
                data_activations_layer[i], self.neighbors)
            try:
                knns_ind[layer][(i), :] = query_res
            except:
                knns_ind[layer][(i), :len(query_res)] = query_res
                knn_errors += knns_ind[layer].shape[1] - len(query_res)
        knns_labels[layer] = np.zeros((nb_data, self.neighbors), dtype=np.int32
            )
        for data_id in range(nb_data):
            knns_labels[layer][(data_id), :] = self.train_labels[knns_ind[
                layer][data_id]]
    return knns_ind, knns_labels