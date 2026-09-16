def search(self, query, delegate, args=None, extra_args=None):
    if args is None:
        args = {}
    args['q'] = query
    return self.__doDownloadPage(self.search_url + '?' + self._urlencode(
        args), txml.Feed(delegate, extra_args), agent=self.agent)