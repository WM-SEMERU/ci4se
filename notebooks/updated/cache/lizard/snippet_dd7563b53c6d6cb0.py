def cookies(self, url):
    part = urlparse(url)
    _domain = part.hostname
    cookie_dict = {}
    now = utc_now()
    for _, a in list(self.cookiejar._cookies.items()):
        for _, b in a.items():
            for cookie in list(b.values()):
                if cookie.expires and cookie.expires <= now:
                    continue
                if not re.search('%s$' % cookie.domain, _domain):
                    continue
                if not re.match(cookie.path, part.path):
                    continue
                cookie_dict[cookie.name] = cookie.value
    return cookie_dict