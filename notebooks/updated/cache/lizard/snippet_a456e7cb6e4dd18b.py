def treeAggregate(self, zeroValue, seqOp, combOp, depth=2):
    if depth < 1:
        raise ValueError('Depth cannot be smaller than 1 but got %d.' % depth)
    if self.getNumPartitions() == 0:
        return zeroValue

    def aggregatePartition(iterator):
        acc = zeroValue
        for obj in iterator:
            acc = seqOp(acc, obj)
        yield acc
    partiallyAggregated = self.mapPartitions(aggregatePartition)
    numPartitions = partiallyAggregated.getNumPartitions()
    scale = max(int(ceil(pow(numPartitions, 1.0 / depth))), 2)
    while numPartitions > scale + numPartitions / scale:
        numPartitions /= scale
        curNumPartitions = int(numPartitions)

        def mapPartition(i, iterator):
            for obj in iterator:
                yield i % curNumPartitions, obj
        partiallyAggregated = partiallyAggregated.mapPartitionsWithIndex(
            mapPartition).reduceByKey(combOp, curNumPartitions).values()
    return partiallyAggregated.reduce(combOp)