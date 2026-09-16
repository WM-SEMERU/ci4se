def switch_name_style(self, http_protocol_version):
    new_headers = WHTTPHeaders()
    new_headers.__normalization_mode = http_protocol_version
    names = self.headers()
    for name in names:
        new_headers.add_headers(name, *self.get_headers(name))
    for cookie_name in self.__set_cookies.cookies():
        new_headers.__set_cookies.add_cookie(self.__set_cookies[cookie_name
            ].copy())
    return new_headers