def load_cookies_file(cookies_file):
    logging.debug('Loading cookie file %s into memory.', cookies_file)
    cookies = StringIO()
    cookies.write('# Netscape HTTP Cookie File')
    cookies.write(open(cookies_file, 'rU').read())
    cookies.flush()
    cookies.seek(0)
    return cookies