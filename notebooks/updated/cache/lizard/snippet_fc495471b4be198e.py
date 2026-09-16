def _pycurl_post(self, url, json=None, data=None, username='', password='',
    headers={}, timeout=30):
    response_headers = {}
    curl = pycurl.Curl()
    curl.setopt(curl.URL, url)
    if sys.version_info[0] >= 3:
        stringbuffer = BytesIO()
    else:
        stringbuffer = StringIO()
    curl.setopt(curl.WRITEDATA, stringbuffer)
    headers['User-Agent'] = self.user_agent
    if sys.version_info[0] >= 3:
        header_list = [('%s:%s' % (k, v)) for k, v in headers.items()]
    else:
        header_list = [('%s:%s' % (k, v)) for k, v in headers.iteritems()]
    if json:
        header_list.append('Content-Type:application/json')
    curl.setopt(pycurl.HTTPHEADER, header_list)
    raw_store = json
    raw_request = json_lib.dumps(json) if json else urlencode(data)
    curl.setopt(curl.POSTFIELDS, raw_request)
    if username and password:
        curl.setopt(curl.USERPWD, '%s:%s' % (username, password))
    curl.setopt(curl.TIMEOUT, timeout)
    curl.perform()
    result = stringbuffer.getvalue()
    status_code = curl.getinfo(curl.RESPONSE_CODE)
    curl.close()
    raw_request = raw_store
    return result, raw_request, status_code, response_headers