def extract_credentials(self, url):
    if isinstance(url, urllib2.Request):
        result = urlparse.urlsplit(url.get_full_url())
    else:
        result = urlparse.urlsplit(url)
    scheme, netloc, path, query, frag = result
    username, password = self.parse_credentials(netloc)
    if username is None:
        return url, None, None
    elif password is None and self.prompting:
        netloc = netloc.replace('%s@' % username, '', 1)
        prompt = 'Password for %s@%s: ' % (username, netloc)
        password = urllib.quote(getpass.getpass(prompt))
    else:
        netloc = netloc.replace('%s:%s@' % (username, password), '', 1)
    target_url = urlparse.urlunsplit((scheme, netloc, path, query, frag))
    return target_url, username, password