def _generate(self, message):
    raw_params = {'INPUT_TEXT': message.encode('UTF8'), 'INPUT_TYPE': self.
        input_type, 'OUTPUT_TYPE': self.output_type, 'LOCALE': self._locale,
        'AUDIO': self.audio, 'VOICE': self._voice}
    params = urlencode(raw_params)
    headers = {}
    logging.debug('maryclient: generate, raw_params=%s' % repr(raw_params))
    conn = httplib.HTTPConnection(self._host, self._port)
    conn.request('POST', '/process', params, headers)
    response = conn.getresponse()
    if response.status != 200:
        logging.error(response.getheaders())
        raise Exception('{0}: {1}'.format(response.status, response.reason))
    return response.read()