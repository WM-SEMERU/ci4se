def _rescale_array(self, array, scale, zero):
    if scale != 1.0:
        sval = numpy.array(scale, dtype=array.dtype)
        array *= sval
    if zero != 0.0:
        zval = numpy.array(zero, dtype=array.dtype)
        array += zval