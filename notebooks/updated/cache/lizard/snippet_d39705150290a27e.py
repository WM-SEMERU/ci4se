def get(self):
    url = self.getUrl()
    for retry in range(3):
        try:
            self.logger.debug('Making request to slick at url %s', url)
            r = requests.get(url)
            self.logger.debug('Request returned status code %d', r.status_code)
            if r.status_code is 200:
                return self.model.from_dict(r.json())
            else:
                self.logger.debug('Body of what slick returned: %s', r.text)
        except BaseException as error:
            self.logger.warn(
                'Received exception while connecting to slick at %s', url,
                exc_info=sys.exc_info())
    raise SlickCommunicationError(
        'Tried 3 times to request data from slick at url %s without a successful status code.'
        , url)