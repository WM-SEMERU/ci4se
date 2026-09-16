def capture(target_url, user_agent=
    'savepagenow (https://github.com/pastpages/savepagenow)', accept_cache=
    False):
    domain = 'https://web.archive.org'
    save_url = urljoin(domain, '/save/')
    request_url = save_url + target_url
    headers = {'User-Agent': user_agent}
    response = requests.get(request_url, headers=headers)
    has_error_header = 'X-Archive-Wayback-Runtime-Error' in response.headers
    if has_error_header:
        error_header = response.headers['X-Archive-Wayback-Runtime-Error']
        if error_header == 'RobotAccessControlException: Blocked By Robots':
            raise BlockedByRobots(
                'archive.org returned blocked by robots.txt error')
        else:
            raise WaybackRuntimeError(error_header)
    if response.status_code in [403, 502]:
        raise WaybackRuntimeError(response.headers)
    try:
        archive_id = response.headers['Content-Location']
    except KeyError:
        raise WaybackRuntimeError(dict(status_code=response.status_code,
            headers=response.headers))
    archive_url = urljoin(domain, archive_id)
    cached = 'X-Page-Cache' in response.headers and response.headers[
        'X-Page-Cache'] == 'HIT'
    if cached:
        if not accept_cache:
            raise CachedPage(
                'archive.org returned a cached version of this page: {}'.
                format(archive_url))
    return archive_url