def get_license_from_url(url):
    if not url:
        return
    split_url = urlsplit(url, scheme='http')
    if split_url.netloc.lower() == 'creativecommons.org':
        if 'publicdomain' in split_url.path:
            match = _RE_PUBLIC_DOMAIN_URL.match(split_url.path)
            if match is None:
                license = ['public domain']
            else:
                license = ['CC0']
                license.extend(part for part in match.groups() if part)
        else:
            license = ['CC']
            match = _RE_LICENSE_URL.match(split_url.path)
            license.extend(part.upper() for part in match.groups() if part)
    elif split_url.netloc == 'arxiv.org':
        license = ['arXiv']
        match = _RE_LICENSE_URL.match(split_url.path)
        license.extend(part for part in match.groups() if part)
    else:
        raise ValueError('Unknown license URL')
    return ' '.join(license)