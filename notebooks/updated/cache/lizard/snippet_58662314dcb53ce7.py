def abs_urls(data, target_url, image_url):

    def replacer(regex, url):
        replacement = '\\1 {0}/\\2'.format(url.rstrip('/'))
        return lambda line: regex.sub(replacement, line, count=1)
    replacers = [replacer(REGEX_ABS_URLS_TARGET, target_url), replacer(
        REGEX_ABS_URLS_IMAGE, image_url)]
    return [functools.reduce(lambda el, func: func(el), replacers, line) for
        line in data]