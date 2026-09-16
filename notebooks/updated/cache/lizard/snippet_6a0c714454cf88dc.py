def _zero_pad_gaps(tr, gaps, fill_gaps=True):
    start_in, end_in = tr.stats.starttime, tr.stats.endtime
    for gap in gaps:
        stream = Stream()
        if gap['starttime'] > tr.stats.starttime:
            stream += tr.slice(tr.stats.starttime, gap['starttime']).copy()
        if gap['endtime'] < tr.stats.endtime:
            stream += tr.slice(gap['endtime'], tr.stats.endtime).copy()
        tr = stream.merge()[0]
    if fill_gaps:
        tr = tr.split()
        tr = tr.detrend()
        tr = tr.merge(fill_value=0)[0]
        if tr.stats.starttime != start_in:
            tr.data = np.concatenate([np.zeros(int(tr.stats.starttime -
                start_in)), tr.data])
            tr.stats.starttime = start_in
        if tr.stats.endtime != end_in:
            tr.data = np.concatenate([tr.data, np.zeros(int(end_in - tr.
                stats.endtime))])
    return tr