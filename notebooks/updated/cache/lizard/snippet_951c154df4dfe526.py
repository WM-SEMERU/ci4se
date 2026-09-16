def get_content(url, user=None, password=None, proxy=None, data=None,
    addheaders=None):
    from . import configuration
    headers = {'User-Agent': configuration.UserAgent}
    if addheaders:
        headers.update(addheaders)
    method = 'GET'
    kwargs = dict(headers=headers)
    if user and password:
        kwargs['auth'] = user, password
    if data:
        kwargs['data'] = data
        method = 'POST'
    if proxy:
        kwargs['proxy'] = dict(http=proxy)
    from .configuration import get_share_file
    try:
        kwargs['verify'] = get_share_file('cacert.pem')
    except ValueError:
        pass
    try:
        response = requests.request(method, url, **kwargs)
        return response.text, response.headers
    except (requests.exceptions.RequestException, requests.exceptions.
        BaseHTTPError) as msg:
        log.warn(LOG_CHECK, 
            'Could not get content of URL %(url)s: %(msg)s.' % {'url': url,
            'msg': str(msg)})
        return None, str(msg)