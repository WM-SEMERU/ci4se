def transfer_session_cookies_to_driver(self, domain=None):
    if not domain and self._last_requests_url:
        domain = tldextract.extract(self._last_requests_url).registered_domain
    elif not domain and not self._last_requests_url:
        raise Exception(
            'Trying to transfer cookies to selenium without specifying a domain and without having visited any page in the current session'
            )
    for c in [c for c in self.cookies if domain in c.domain]:
        self.driver.ensure_add_cookie({'name': c.name, 'value': c.value,
            'path': c.path, 'expiry': c.expires, 'domain': c.domain})