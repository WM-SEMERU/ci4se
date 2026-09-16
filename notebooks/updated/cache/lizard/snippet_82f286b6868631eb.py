def escape_url(url, lowercase_urlencoding=False):
    encoded = quote_plus(url)
    return re.sub('%[A-F0-9]{2}', lambda m: m.group(0).lower(), encoded
        ) if lowercase_urlencoding else encoded