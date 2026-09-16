def _query(self, url=None, params=''):
    if url is None:
        raise NoUrlError('No URL was provided.')
    headers = {'location': None, 'title': None}
    headerdata = urllib.urlencode(params)
    try:
        request = urllib2.Request(url, headerdata)
        response = urllib2.urlopen(request)
        if 'jsonp' in params:
            status = response.read()
        else:
            status = response.getcode()
        info = response.info()
        try:
            headers['location'] = info['Content-Location']
        except KeyError:
            pass
        try:
            headers['title'] = info['X-Instapaper-Title']
        except KeyError:
            pass
        return status, headers
    except urllib2.HTTPError as exception:
        if 'jsonp' in params:
            return '%s({"status":%d})' % (params['jsonp'], exception.code
                ), headers
        else:
            return exception.code, headers
    except IOError as exception:
        return exception.code, headers