def loadLabeledPoints(sc, path, minPartitions=None):
    minPartitions = minPartitions or min(sc.defaultParallelism, 2)
    return callMLlibFunc('loadLabeledPoints', sc, path, minPartitions)