def url_to_host(url):
    regex_url = ('([a-z][a-z0-9+\\-.]*://)?' +
        "([a-z0-9\\-._~%!$&'()*+,;=]+@)?" + '([a-z0-9\\-._~%]+' +
        "|\\[[a-z0-9\\-._~%!$&'()*+,;=:]+\\])?" + '(:(?P<port>[0-9]+))?')
    m = re.match(regex_url, url, re.IGNORECASE)
    if m and m.group(3):
        return url[m.start(3):m.end(3)]
    else:
        raise ValueError('URL without a valid host or ip')