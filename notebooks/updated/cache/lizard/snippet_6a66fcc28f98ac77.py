def flatten4d3d(x):
    xshape = shape_list(x)
    result = tf.reshape(x, [xshape[0], xshape[1] * xshape[2], xshape[3]])
    return result