def setup_url(self, url):
    r
    self.url = bytes(url, 'utf8')
    res = librtmp.RTMP_SetupURL(self.rtmp, self.url)
    if res < 1:
        raise RTMPError('Unable to parse URL')