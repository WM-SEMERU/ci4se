def sorted_fancy_indexing(indexable, request):
    if len(request) > 1:
        indices = numpy.argsort(request)
        data = numpy.empty(shape=(len(request),) + indexable.shape[1:],
            dtype=indexable.dtype)
        data[indices] = indexable[numpy.array(request)[indices], ...]
    else:
        data = indexable[request]
    return data