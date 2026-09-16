def get_max_counts(samples):
    counts = []
    for data in (x[0] for x in samples):
        count = tz.get_in(['config', 'algorithm', 'callable_count'], data, 1)
        vcs = tz.get_in(['config', 'algorithm', 'variantcaller'], data, [])
        if isinstance(vcs, six.string_types):
            vcs = [vcs]
        if vcs:
            count *= len(vcs)
        counts.append(count)
    return max(counts)