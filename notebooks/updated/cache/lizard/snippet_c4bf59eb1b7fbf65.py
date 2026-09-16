def parse_esmtp_extensions(message):
    extns = {}
    auths = []
    oldstyle_auth_regex = re.compile('auth=(?P<auth>.*)', re.IGNORECASE)
    extension_regex = re.compile('(?P<feature>[a-z0-9][a-z0-9\\-]*) ?', re.
        IGNORECASE)
    lines = message.splitlines()
    for line in lines[1:]:
        match = oldstyle_auth_regex.match(line)
        if match:
            auth = match.group('auth')[0]
            auth = auth.lower().strip()
            if auth not in auths:
                auths.append(auth)
        match = extension_regex.match(line)
        if match:
            feature = match.group('feature').lower()
            params = match.string[match.end('feature'):].strip()
            extns[feature] = params
            if feature == 'auth':
                auths.extend([param.strip().lower() for param in params.
                    split()])
    return extns, auths