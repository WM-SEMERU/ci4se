def humanize_time_delta(sec):
    if sec < 0:
        logger.warn('humanize_time_delta() obtains negative seconds!')
        return '{:.3g} seconds'.format(sec)
    if sec == 0:
        return '0 second'
    time = datetime(2000, 1, 1) + timedelta(seconds=int(sec))
    units = ['day', 'hour', 'minute', 'second']
    vals = [int(sec // 86400), time.hour, time.minute, time.second]
    if sec < 60:
        vals[-1] = sec

    def _format(v, u):
        return '{:.3g} {}{}'.format(v, u, 's' if v > 1 else '')
    ans = []
    for v, u in zip(vals, units):
        if v > 0:
            ans.append(_format(v, u))
    return ' '.join(ans)