def remove_cookie_by_name(cookiejar, name, domain=None, path=None):
    clearables = []
    for cookie in cookiejar:
        if cookie.name != name:
            continue
        if domain is not None and domain != cookie.domain:
            continue
        if path is not None and path != cookie.path:
            continue
        clearables.append((cookie.domain, cookie.path, cookie.name))
    for domain, path, name in clearables:
        cookiejar.clear(domain, path, name)