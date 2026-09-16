def neighbor_difference(self):
    differences = np.zeros(self.num_neurons)
    num_neighbors = np.zeros(self.num_neurons)
    distance, _ = self.distance_function(self.weights, self.weights)
    for x, y in self.neighbors():
        differences[x] += distance[x, y]
        num_neighbors[x] += 1
    return differences / num_neighbors