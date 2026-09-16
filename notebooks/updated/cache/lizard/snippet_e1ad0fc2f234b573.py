def label(self, string):
    if '*/' in string:
        raise ValueError('Bad label - cannot be embedded in SQL comment')
    return self.extra(where=["/*QueryRewrite':label={}*/1".format(string)])