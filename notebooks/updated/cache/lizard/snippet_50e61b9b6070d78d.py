def instant_articles(self, **kwargs):
    eqs = self.search(**kwargs).sort('-last_modified', '-published')
    return eqs.filter(InstantArticle())