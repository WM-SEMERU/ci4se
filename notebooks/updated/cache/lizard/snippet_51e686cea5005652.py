def cleanup(arg):
    arg = numpy.asarray(arg)
    if len(arg.shape) <= 1:
        arg = arg.reshape(arg.size, 1)
    elif len(arg.shape) > 2:
        raise ValueError('shapes must be smaller than 3')
    return arg