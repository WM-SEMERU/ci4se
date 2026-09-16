def proxy(self):
    headers = self.request.headers.filter(self.ignored_request_headers)
    qs = self.request.query_string if self.pass_query_string else ''
    if self.request.META.get('CONTENT_LENGTH', None
        ) == '' and get_django_version() == '1.10':
        del self.request.META['CONTENT_LENGTH']
    request_kwargs = self.middleware.process_request(self, self.request,
        method=self.request.method, url=self.proxy_url, headers=headers,
        data=self.request.body, params=qs, allow_redirects=False, verify=
        self.verify_ssl, cert=self.cert, timeout=self.timeout)
    result = request(**request_kwargs)
    response = HttpResponse(result.content, status=result.status_code)
    forwardable_headers = HeaderDict(result.headers).filter(self.
        ignored_upstream_headers)
    for header, value in iteritems(forwardable_headers):
        response[header] = value
    return self.middleware.process_response(self, self.request, result,
        response)