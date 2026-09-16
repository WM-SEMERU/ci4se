def is_parsable(url):
    try:
        parsed = urlparse(url)
        URLHelper.__cache[url] = parsed
        return True
    except:
        return False