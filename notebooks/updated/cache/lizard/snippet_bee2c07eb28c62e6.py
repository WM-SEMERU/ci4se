def filter_url(pkg_type, url):
    bad_stuff = ['?modtime', '#md5=']
    for junk in bad_stuff:
        if junk in url:
            url = url.split(junk)[0]
            break
    if url.endswith('-dev'):
        url = url.split('#egg=')[0]
    if pkg_type == 'all':
        return url
    elif pkg_type == 'source':
        valid_source_types = ['.tgz', '.tar.gz', '.zip', '.tbz2', '.tar.bz2']
        for extension in valid_source_types:
            if url.lower().endswith(extension):
                return url
    elif pkg_type == 'egg':
        if url.lower().endswith('.egg'):
            return url