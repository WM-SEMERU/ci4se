def _merge_close(dat, events, time, min_interval):
    if not events.any():
        return events
    no_merge = time[events[1:, (0)] - 1] - time[events[:-1, (2)]
        ] >= min_interval
    if no_merge.any():
        begs = concatenate([[events[0, 0]], events[1:, (0)][no_merge]])
        ends = concatenate([events[:-1, (2)][no_merge], [events[-1, 2]]])
        new_events = vstack((begs, ends)).T
    else:
        new_events = asarray([[events[0, 0], events[-1, 2]]])
    new_events = insert(new_events, 1, 0, axis=1)
    for i in new_events:
        if i[2] - i[0] >= 1:
            i[1] = i[0] + argmax(dat[i[0]:i[2]])
    return new_events