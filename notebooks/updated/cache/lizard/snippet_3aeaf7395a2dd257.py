def mentions_links(uri, s):
    for username, after in mentions_re.findall(s):
        _uri = '/' + (uri or '').lstrip('/') + quote(username)
        link = '<a href="{}">@{}</a>{}'.format(_uri.lower(), username, after)
        s = s.replace('@' + username, link)
    return s