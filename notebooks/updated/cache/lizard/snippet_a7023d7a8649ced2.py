def mae(x_values, y_values, drop_missing=True):
    num_points = len(x_values)
    assert num_points == len(y_values) and num_points > 0
    return numpy.sum(numpy.apply_along_axis(numpy.abs, 0, numpy.subtract(
        x_values, y_values))) / float(num_points)