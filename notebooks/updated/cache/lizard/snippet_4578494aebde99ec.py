def take_along_axis(large_array, indexes):
    if len(large_array.shape) > len(indexes.shape):
        indexes = indexes.reshape(indexes.shape + tuple([1] * (len(
            large_array.shape) - len(indexes.shape))))
    return np.take_along_axis(large_array, indexes, axis=0)