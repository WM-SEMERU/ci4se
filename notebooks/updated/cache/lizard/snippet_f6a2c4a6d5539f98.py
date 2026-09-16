def show_user(self, user):
    url = '/users/show/%s.xml' % user
    d = defer.Deferred()
    self.__downloadPage(url, txml.Users(lambda u: d.callback(u))).addErrback(
        lambda e: d.errback(e))
    return d