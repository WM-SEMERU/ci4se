def request(self, request, proxies, timeout, verify, **_):
    settings = self.http.merge_environment_settings(request.url, proxies,
        False, verify, None)
    return self.http.send(request, timeout=timeout, allow_redirects=False,
        **settings)