def LCP(SA):
    string = SA.string
    length = SA.length
    lcps = _array('i', [0] * length)
    SA = SA.SA
    if _trace:
        delta = max(length // 100, 1)
        for i, pos in enumerate(SA):
            if i % delta == 0:
                percent = float((i + 1) * 100) / length
                print >> _stderr, 'Compute_LCP %.2f%% (%i/%i)\r' % (percent,
                    i + 1, length)
            lcps[i] = _longestCommonPrefix(string, string, SA[i - 1], pos)
    else:
        for i, pos in enumerate(SA):
            lcps[i] = _longestCommonPrefix(string, string, SA[i - 1], pos)
    if _trace:
        print >> _stderr, 'Compute_LCP %.2f%% (%i/%i)\r' % (100.0, length,
            length)
    if lcps:
        lcps[0] = 0
    return lcps