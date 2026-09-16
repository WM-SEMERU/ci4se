def GET(self, url):
    r = requests.get(url)
    if self.verbose:
        sys.stdout.write('%s %s\n' % (r.status_code, r.encoding))
        sys.stdout.write(str(r.headers) + '\n')
    self.encoding = r.encoding
    return r.text