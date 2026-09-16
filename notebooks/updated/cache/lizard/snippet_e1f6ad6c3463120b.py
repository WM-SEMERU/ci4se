def request(self, url, method, data=None, headers=None):
    http_headers = merge_dict(self.default_headers, headers or {})
    request_data = merge_dict({'api_key': self.apikey}, data or {})
    logger.info('HTTP %s REQUEST TO %s' % (method, url))
    start = datetime.datetime.now()
    try:
        response = requests.request(method=method, url=url, data=json.dumps
            (request_data), headers=http_headers)
    except exceptions.BadRequestError as e:
        return json.loads({'errors': e.content})
    duration = datetime.datetime.now() - start
    logger.info('RESPONSE %s DURATION %s.%s' % (response.encoding, duration
        .seconds, duration.microseconds))
    return json.loads(response.content) if response.content else {}