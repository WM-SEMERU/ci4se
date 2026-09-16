def subscribe(self, callback_url, timeout=None):
    url = urljoin(self._url_base, self._event_sub_url)
    headers = dict(HOST=urlparse(url).netloc, CALLBACK='<%s>' %
        callback_url, NT='upnp:event')
    if timeout is not None:
        headers['TIMEOUT'] = 'Second-%s' % timeout
    resp = requests.request('SUBSCRIBE', url, headers=headers, auth=self.
        device.http_auth)
    resp.raise_for_status()
    return Service.validate_subscription_response(resp)