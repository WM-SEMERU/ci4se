def _local_decode(self):
    decoded_result_assignment = {node: np.argmax(self.objective[node].
        values) for node in self.objective if len(node) == 1}
    integer_value = sum([self.factors[variable][0].values[
        decoded_result_assignment[frozenset([variable])]] for variable in
        self.variables])
    for cluster_key in self.cluster_set:
        cluster = self.cluster_set[cluster_key]
        index = [tuple([variable, decoded_result_assignment[frozenset([
            variable])]]) for variable in cluster.cluster_variables]
        integer_value += cluster.cluster_potential.reduce(index, inplace=False
            ).values
    if self.best_int_objective < integer_value:
        self.best_int_objective = integer_value
        self.best_assignment = decoded_result_assignment