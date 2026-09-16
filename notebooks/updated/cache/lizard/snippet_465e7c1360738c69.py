def parse_headers(self, http_code):
    if self.__ro_flag:
        raise RuntimeError('Read-only object changing attempt')
    self.__headers = WHTTPHeaders.import_headers(http_code)