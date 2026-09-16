def last_modified(self):
    lm = self.response.headers.get('last-modified', None)
    return datetime.strptime(lm, '%a, %d %b %Y %H:%M:%S GMT') if lm else None