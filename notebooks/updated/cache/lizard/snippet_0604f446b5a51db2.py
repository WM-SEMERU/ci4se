def optimise_partition_multiplex(self, partitions, layer_weights=None):
    if not layer_weights:
        layer_weights = [1] * len(partitions)
    diff = _c_louvain._Optimiser_optimise_partition_multiplex(self.
        _optimiser, [partition._partition for partition in partitions],
        layer_weights)
    for partition in partitions:
        partition._update_internal_membership()
    return diff