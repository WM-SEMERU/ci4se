def make_retrigger_request(repo_name, request_id, auth, count=
    DEFAULT_COUNT_NUM, priority=DEFAULT_PRIORITY, dry_run=True):
    url = '{}/{}/request'.format(SELF_SERVE, repo_name)
    payload = {'request_id': request_id}
    if count != DEFAULT_COUNT_NUM or priority != DEFAULT_PRIORITY:
        payload.update({'count': count, 'priority': priority})
    if dry_run:
        LOG.info('We would make a POST request to %s with the payload: %s' %
            (url, str(payload)))
        return None
    LOG.info(
        "We're going to re-trigger an existing completed job with request_id: %s %i time(s)."
         % (request_id, count))
    req = requests.post(url, headers={'Accept': 'application/json'}, data=
        payload, auth=auth, timeout=TCP_TIMEOUT)
    return req