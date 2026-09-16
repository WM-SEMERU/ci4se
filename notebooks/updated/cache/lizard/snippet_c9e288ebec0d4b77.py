def refresh_db(cache_valid_time=0, failhard=False, **kwargs):
    salt.utils.pkg.clear_rtag(__opts__)
    failhard = salt.utils.data.is_true(failhard)
    ret = {}
    error_repos = list()
    if cache_valid_time:
        try:
            latest_update = os.stat(APT_LISTS_PATH).st_mtime
            now = time.time()
            log.debug('now: %s, last update time: %s, expire after: %s seconds'
                , now, latest_update, cache_valid_time)
            if latest_update + cache_valid_time > now:
                return ret
        except TypeError as exp:
            log.warning(
                'expected integer for cache_valid_time parameter, failed with: %s'
                , exp)
        except IOError as exp:
            log.warning('could not stat cache directory due to: %s', exp)
    call = _call_apt(['apt-get', '-q', 'update'], scope=False)
    if call['retcode'] != 0:
        comment = ''
        if 'stderr' in call:
            comment += call['stderr']
        raise CommandExecutionError(comment)
    else:
        out = call['stdout']
    for line in out.splitlines():
        cols = line.split()
        if not cols:
            continue
        ident = ' '.join(cols[1:])
        if 'Get' in cols[0]:
            ident = re.sub(' \\[.+B\\]$', '', ident)
            ret[ident] = True
        elif 'Ign' in cols[0]:
            ret[ident] = False
        elif 'Hit' in cols[0]:
            ret[ident] = None
        elif 'Err' in cols[0]:
            ret[ident] = False
            error_repos.append(ident)
    if failhard and error_repos:
        raise CommandExecutionError('Error getting repos: {0}'.format(', '.
            join(error_repos)))
    return ret