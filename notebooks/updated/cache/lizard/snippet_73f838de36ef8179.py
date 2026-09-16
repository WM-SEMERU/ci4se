def unbroadcast_numpy_to(array, shape):
    axis = create_unbroadcast_axis(shape, numpy.shape(array))
    return numpy.reshape(numpy.sum(array, axis=axis), shape)