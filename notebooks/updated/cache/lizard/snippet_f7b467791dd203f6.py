def update(self):
    obj = self.data
    url = self.getUrl()
    last_stats_code = None
    last_body = None
    for retry in range(3):
        try:
            json_data = obj.to_json()
            self.logger.debug(
                'Making request to slick at url %s, with data: %s', url,
                json_data)
            r = requests.put(url, data=json_data, headers=json_content)
            self.logger.debug('Request returned status code %d', r.status_code)
            if r.status_code is 200:
                return self.model.from_dict(r.json())
            else:
                last_stats_code = r.status_code
                last_body = r.text
                self.logger.warn('Slick status code: %d', r.status_code)
                self.logger.warn('Body of what slick returned: %s', r.text)
        except BaseException as error:
            self.logger.warn(
                'Received exception while connecting to slick at %s', url,
                exc_info=sys.exc_info())
            traceback.print_exc()
    raise SlickCommunicationError(
        'Tried 3 times to request data from slick at url %s without a successful status code.  Last status code: %d, body: %s'
        , url, last_stats_code, last_body)