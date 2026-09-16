def search(self, search):
    search = search.replace('/', ' ')
    params = {'q': search}
    return self._get_records(params)