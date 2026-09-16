def build(self, builder):
    if self.text is None:
        raise ValueError('Text is not set.')
    params = {}
    if self.sponsor_or_site is not None:
        params['SponsorOrSite'] = self.sponsor_or_site
    builder.start('Comment', params)
    builder.data(self.text)
    builder.end('Comment')