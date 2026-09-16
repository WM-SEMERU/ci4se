def cookiejar_from_dict(*cookie_dicts):
    cookie_dicts = tuple(d for d in cookie_dicts if d)
    if len(cookie_dicts) == 1 and isinstance(cookie_dicts[0], CookieJar):
        return cookie_dicts[0]
    cookiejar = CookieJar()
    for cookie_dict in cookie_dicts:
        if isinstance(cookie_dict, CookieJar):
            for cookie in cookie_dict:
                cookiejar.set_cookie(cookie)
        else:
            for name in cookie_dict:
                cookiejar.set_cookie(create_cookie(name, cookie_dict[name]))
    return cookiejar