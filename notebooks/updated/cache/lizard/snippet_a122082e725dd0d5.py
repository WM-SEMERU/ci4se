def _find_next(server):
    from datetime import datetime
    _load_db()
    result = None
    visited = []
    if 'status' in db:
        for reponame, status in db['status'].items():
            vms('Checking cron status for {}: {}'.format(reponame, status))
            start = None if 'started' not in status else status['started']
            end = None if 'end' not in status else status['end']
            running = start is not None and end is not None and start > end
            add = False
            if not running and end is not None:
                elapsed = (datetime.now() - end).seconds / 60
                add = elapsed > server.cron.settings[reponame].frequency
                if not add:
                    vms("'{}' skipped because the interval hasn't ".format(
                        reponame) + 'elapsed ({} vs. {})'.format(elapsed,
                        server.cron.settings[reponame].frequency))
            elif end is None:
                add = True
            if add:
                result = reponame
                break
            visited.append(reponame)
    else:
        db['status'] = {}
    if result is None:
        for reponame, repo in server.repositories.items():
            if reponame not in visited:
                vms("Added '{}' as new repo for cron execution.".format(
                    reponame))
                result = reponame
                break
    return result