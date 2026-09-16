def least_upper_bound(*intervals_to_join):
    assert len(intervals_to_join) > 0, 'No intervals to join'
    all_same = all(x.bits == intervals_to_join[0].bits for x in
        intervals_to_join)
    assert all_same, 'All intervals to join should be same'
    if len(intervals_to_join) == 1:
        return intervals_to_join[0].copy()
    if len(intervals_to_join) == 2:
        return StridedInterval.pseudo_join(intervals_to_join[0],
            intervals_to_join[1])
    sorted_intervals = sorted(intervals_to_join, key=lambda x: x.lower_bound)
    ret = None
    for i in xrange(len(sorted_intervals)):
        si = reduce(lambda x, y: StridedInterval.pseudo_join(x, y, False), 
            sorted_intervals[i:] + sorted_intervals[0:i])
        if ret is None or ret.n_values > si.n_values:
            ret = si
    if any([x for x in intervals_to_join if x.uninitialized]):
        ret.uninitialized = True
    return ret