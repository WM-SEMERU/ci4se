def compress_histogram(buckets, bps=NORMAL_HISTOGRAM_BPS):
    buckets = np.array(buckets)
    if not buckets.size:
        return [CompressedHistogramValue(b, 0.0) for b in bps]
    minmin, maxmax = buckets[0][0], buckets[-1][1]
    counts = buckets[:, (2)]
    right_edges = list(buckets[:, (1)])
    weights = (counts * bps[-1] / (counts.sum() or 1.0)).cumsum()
    result = []
    bp_index = 0
    while bp_index < len(bps):
        i = np.searchsorted(weights, bps[bp_index], side='right')
        while i < len(weights):
            cumsum = weights[i]
            cumsum_prev = weights[i - 1] if i > 0 else 0.0
            if cumsum == cumsum_prev:
                i += 1
                continue
            if not i or not cumsum_prev:
                lhs = minmin
            else:
                lhs = max(right_edges[i - 1], minmin)
            rhs = min(right_edges[i], maxmax)
            weight = _lerp(bps[bp_index], cumsum_prev, cumsum, lhs, rhs)
            result.append(CompressedHistogramValue(bps[bp_index], weight))
            bp_index += 1
            break
        else:
            break
    while bp_index < len(bps):
        result.append(CompressedHistogramValue(bps[bp_index], maxmax))
        bp_index += 1
    return result