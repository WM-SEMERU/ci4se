def all_partitions(indices):
    n = len(indices)
    partitions = _partitions_list(n)
    if n > 0:
        partitions[-1] = [list(range(n))]
    for partition in partitions:
        yield tuple(tuple(indices[i] for i in part) for part in partition)