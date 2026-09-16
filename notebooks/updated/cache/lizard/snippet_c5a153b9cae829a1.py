def search_position(**kwargs):
    base_url = 'http://asterank.com/api/skymorph/search_position?'
    for key in kwargs:
        base_url += str(key) + '=' + kwargs[key] + '&'
    base_url = base_url[:-1]
    return dispatch_http_get(base_url)