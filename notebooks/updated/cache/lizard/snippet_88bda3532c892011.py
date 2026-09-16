def get_submissions(self, fullnames, *args, **kwargs):
    fullnames = fullnames[:]
    while fullnames:
        cur = fullnames[:100]
        fullnames[:100] = []
        url = self.config['by_id'] + ','.join(cur)
        for item in self.get_content(url, *args, limit=len(cur), **kwargs):
            yield item