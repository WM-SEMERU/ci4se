def closest_to_ref(arrays, ref, cutoff=1e-12):
    dist = numpy.zeros(len(arrays))
    logref = log(ref, cutoff)
    for rlz, array in enumerate(arrays):
        diff = log(array, cutoff) - logref
        dist[rlz] = numpy.sqrt((diff * diff).sum())
    rlz = dist.argmin()
    closest = dict(rlz=rlz, value=arrays[rlz], dist=dist[rlz])
    return closest