def get_all_names(offset=None, count=None, include_expired=False, proxy=
    None, hostport=None):
    assert proxy or hostport, 'Need proxy or hostport'
    if proxy is None:
        proxy = connect_hostport(hostport)
    offset = 0 if offset is None else offset
    if count is None:
        count = get_num_names(proxy=proxy, hostport=hostport)
        if json_is_error(count):
            return count
        count -= offset
    page_size = 100
    all_names = []
    while len(all_names) < count:
        request_size = page_size
        if count - len(all_names) < request_size:
            request_size = count - len(all_names)
        page = get_all_names_page(offset + len(all_names), request_size,
            include_expired=include_expired, proxy=proxy, hostport=hostport)
        if json_is_error(page):
            return page
        if len(page) > request_size:
            error_str = 'server replied too much data'
            return {'error': error_str, 'http_status': 503}
        elif len(page) == 0:
            break
        all_names += page
    return all_names