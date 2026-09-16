def to_java_rdd(jsc, features, labels, batch_size):
    data_sets = java_classes.ArrayList()
    num_batches = int(len(features) / batch_size)
    for i in range(num_batches):
        xi = ndarray(features[:batch_size].copy())
        yi = ndarray(labels[:batch_size].copy())
        data_set = java_classes.DataSet(xi.array, yi.array)
        data_sets.add(data_set)
        features = features[batch_size:]
        labels = labels[batch_size:]
    return jsc.parallelize(data_sets)