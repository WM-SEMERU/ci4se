def from_url(reddit_session, url, comment_limit=0, comment_sort=None,
    comments_only=False, params=None):
    if params is None:
        params = {}
    parsed = urlparse(url)
    query_pairs = parse_qs(parsed.query)
    get_params = dict((k, ','.join(v)) for k, v in query_pairs.items())
    params.update(get_params)
    url = urlunparse(parsed[:3] + ('', '', ''))
    if comment_limit is None:
        params['limit'] = 2048
    elif comment_limit > 0:
        params['limit'] = comment_limit
    if comment_sort:
        params['sort'] = comment_sort
    response = reddit_session.request_json(url, params=params)
    if comments_only:
        return response[1]['data']['children']
    submission = Submission.from_json(response)
    submission._comment_sort = comment_sort
    submission._params = params
    return submission