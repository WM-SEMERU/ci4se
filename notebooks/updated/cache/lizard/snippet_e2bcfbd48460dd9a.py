def ro(self):
    ro_headers = WHTTPHeaders()
    names = self.headers()
    for name in names:
        ro_headers.add_headers(name, *self.get_headers(name))
    ro_headers.__cookies = self.__set_cookies.ro()
    ro_headers.__ro_flag = True
    return ro_headers