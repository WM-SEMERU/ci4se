def fetch(self):
    start = datetime.now()
    r = requests.get(self._url(), auth=(self.key, ''))
    self._delay_for_ratelimits(start)
    if r.status_code not in self.TRUTHY_CODES:
        return self._handle_request_exception(r)
    response = r.json()
    if self.ENVELOPE:
        self.data = response.get(self.ENVELOPE, {})
    else:
        self.data = response
    self._process_meta(response)