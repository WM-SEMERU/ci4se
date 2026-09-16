def smooth_line_data(data, numpoints, sumcounts=True):
    smoothed = {}
    for s_name, d in data.items():
        if len(d) <= numpoints:
            smoothed[s_name] = d
            continue
        smoothed[s_name] = OrderedDict()
        p = 0
        binsize = len(d) / numpoints
        if binsize < 1:
            binsize = 1
        binvals = []
        for x in sorted(d):
            y = d[x]
            if p < binsize:
                binvals.append(y)
                p += 1
            else:
                if sumcounts is True:
                    v = sum(binvals)
                else:
                    v = sum(binvals) / binsize
                smoothed[s_name][x] = v
                p = 0
                binvals = []
    return smoothed