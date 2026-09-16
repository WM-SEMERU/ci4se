def get(self, title):
    key = '/library/sections/%s/all' % self.key
    return self.fetchItem(key, title__iexact=title)