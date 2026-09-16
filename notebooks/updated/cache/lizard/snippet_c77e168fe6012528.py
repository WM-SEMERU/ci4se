def all(self, **args):
    limit = args['limit'] if 'limit' in args else 20
    offset = args['offset'] if 'offset' in args else 0
    r = requests.get('https://kippt.com/api/lists?limit=%s&offset=%s' % (
        limit, offset), headers=self.kippt.header)
    return r.json()