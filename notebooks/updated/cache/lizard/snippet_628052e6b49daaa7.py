def _partitions_list(N):
    if N < _NUM_PRECOMPUTED_PARTITION_LISTS:
        return list(_partition_lists[N])
    else:
        raise ValueError(
            'Partition lists not yet available for system with {} nodes or more'
            .format(_NUM_PRECOMPUTED_PARTITION_LISTS))