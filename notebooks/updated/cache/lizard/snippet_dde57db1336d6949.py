def linstack(streams, normalize=True):
    stack = streams[np.argmax([len(stream) for stream in streams])].copy()
    if normalize:
        for tr in stack:
            tr.data = tr.data / np.sqrt(np.mean(np.square(tr.data)))
            tr.data = np.nan_to_num(tr.data)
    for i in range(1, len(streams)):
        for tr in stack:
            matchtr = streams[i].select(station=tr.stats.station, channel=
                tr.stats.channel)
            if matchtr:
                if normalize:
                    norm = matchtr[0].data / np.sqrt(np.mean(np.square(
                        matchtr[0].data)))
                    norm = np.nan_to_num(norm)
                else:
                    norm = matchtr[0].data
                tr.data = np.sum((norm, tr.data), axis=0)
    return stack