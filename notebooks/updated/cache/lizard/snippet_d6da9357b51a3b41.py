def _longer_than(segments, min_dur):
    if min_dur <= 0.0:
        return segments
    long_enough = []
    for seg in segments:
        if sum([(t[1] - t[0]) for t in seg['times']]) >= min_dur:
            long_enough.append(seg)
    return long_enough