def _calculate_status(self, target_freshness, freshness):
    for key in ('error', 'warn'):
        fullkey = '{}_after'.format(key)
        if fullkey not in target_freshness:
            continue
        target = target_freshness[fullkey]
        kwname = target['period'] + 's'
        kwargs = {kwname: target['count']}
        if freshness > timedelta(**kwargs).total_seconds():
            return key
    return 'pass'