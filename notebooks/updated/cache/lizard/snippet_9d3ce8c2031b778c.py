def cookie_length(self, domain):
    cookies = self.cookie_jar._cookies
    if domain not in cookies:
        return 0
    length = 0
    for path in cookies[domain]:
        for name in cookies[domain][path]:
            cookie = cookies[domain][path][name]
            length += len(path) + len(name) + len(cookie.value or '')
    return length