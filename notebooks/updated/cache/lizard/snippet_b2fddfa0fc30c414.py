def _fetch(self, uri, sub_domain=False):
    url = self._build_request_url(uri, sub_domain=sub_domain)
    try:
        res = self.request_handler.send('HEAD', url=url, allow_redirects=
            self.follow_redirects)
        if res.status_code not in self.ignored_error_codes:
            self._log_response(res.status_code, url, res.headers)
    except (AttributeError, RequestHandlerException):
        pass