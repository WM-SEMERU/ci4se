def find(self, query=None, **kwargs):
    url = self.getUrl()
    if query is not None:
        if isinstance(query, queries.SlickQuery):
            url = url + '?' + urlencode(query.to_dict())
        elif isinstance(query, dict):
            url = url + '?' + urlencode(query)
    elif len(kwargs) > 0:
        url = url + '?' + urlencode(kwargs)
    for retry in range(3):
        try:
            self.logger.debug('Making request to slick at url %s', url)
            r = requests.get(url)
            self.logger.debug('Request returned status code %d', r.status_code)
            if r.status_code is 200:
                retval = []
                objects = r.json()
                for dct in objects:
                    retval.append(self.model.from_dict(dct))
                return retval
            else:
                self.logger.error(
                    'Slick returned an error when trying to access %s: status code %s'
                     % (url, str(r.status_code)))
                self.logger.error('Slick response: ', pprint.pformat(r))
        except BaseException as error:
            self.logger.warn(
                'Received exception while connecting to slick at %s', url,
                exc_info=sys.exc_info())
    raise SlickCommunicationError(
        'Tried 3 times to request data from slick at url %s without a successful status code.'
        , url)