def grouped_t(wrap, size):
    return Transformation('grouped({0})'.format(size), partial(grouped_impl,
        wrap, size), None)