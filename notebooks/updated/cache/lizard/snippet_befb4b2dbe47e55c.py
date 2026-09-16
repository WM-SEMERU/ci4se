def _update_triangles(self, triangles_list):
    new_intersection_set = []
    for triangle_vars in triangles_list:
        cardinalities = [self.cardinality[variable] for variable in
            triangle_vars]
        current_intersection_set = [frozenset(intersect) for intersect in
            it.combinations(triangle_vars, 2)]
        current_factor = DiscreteFactor(triangle_vars, cardinalities, np.
            zeros(np.prod(cardinalities)))
        self.cluster_set[frozenset(triangle_vars)] = self.Cluster(
            current_intersection_set, current_factor)
        self.model.factors.append(current_factor)
        new_intersection_set.extend(current_intersection_set)
        self.objective[frozenset(triangle_vars)] = current_factor