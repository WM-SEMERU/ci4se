def coalescence_waiting_times(self, backward=True):
    if not isinstance(backward, bool):
        raise TypeError('backward must be a bool')
    times = list()
    lowest_leaf_dist = float('-inf')
    for n, d in self.distances_from_root():
        if len(n.children) > 1:
            times.append(d)
        elif len(n.children) == 0 and d > lowest_leaf_dist:
            lowest_leaf_dist = d
    times.append(lowest_leaf_dist)
    times.sort(reverse=backward)
    for i in range(len(times) - 1):
        yield abs(times[i] - times[i + 1])