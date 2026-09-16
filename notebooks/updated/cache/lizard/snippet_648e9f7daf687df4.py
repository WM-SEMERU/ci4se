def write_data(self, key, data, tags=[], attrs={}):
    url = make_series_url(key)
    url = urlparse.urljoin(url + '/', 'data')
    dlist = [d.to_dictionary() for d in data]
    body = json.dumps(dlist)
    resp = self.session.post(url, body)
    return resp