def start_session(self):
    if self.has_active_session():
        raise Exception('Session already in progress.')
    response = requests.post(self._get_login_url(), headers=self.
        _get_login_headers(), data=self._get_login_xml())
    response.raise_for_status()
    root = ET.fromstring(response.text)
    for e in root.iter('%ssessionId' % self.SOAP_NS):
        if self.session_id:
            raise Exception(
                'Invalid login attempt.  Multiple session ids found.')
        self.session_id = e.text
    for e in root.iter('%sserverUrl' % self.SOAP_NS):
        if self.server_url:
            raise Exception(
                'Invalid login attempt.  Multiple server urls found.')
        self.server_url = e.text
    if not self.has_active_session():
        raise Exception(
            'Invalid login attempt resulted in null sessionId [%s] and/or serverUrl [%s].'
             % (self.session_id, self.server_url))
    self.hostname = urlsplit(self.server_url).hostname