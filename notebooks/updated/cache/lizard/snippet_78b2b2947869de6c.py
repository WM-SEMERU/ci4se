def search(self, keyword, types=[], terr=KKBOXTerritory.TAIWAN):
    url = 'https://api.kkbox.com/v1.1/search'
    url += '?' + url_parse.urlencode({'q': keyword, 'territory': terr})
    if len(types) > 0:
        url += '&type=' + ','.join(types)
    return self.http._post_data(url, None, self.http.
        _headers_with_access_token())