def parse(self, fp, headersonly=False):
    feedparser = FeedParser(self._class, policy=self.policy)
    if headersonly:
        feedparser._set_headersonly()
    while True:
        data = fp.read(8192)
        if not data:
            break
        feedparser.feed(data)
    return feedparser.close()