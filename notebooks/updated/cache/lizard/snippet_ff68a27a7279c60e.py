def starred(self, **args):
    ids = []
    r = requests.get('%s/gists/starred' % BASE_URL, headers=self.gist.header)
    if 'limit' in args:
        limit = args['limit']
    else:
        limit = len(r.json())
    if r.status_code == 200:
        for g in range(0, limit):
            ids.append('%s/%s/%s' % (GIST_URL, r.json()[g]['user']['login'],
                r.json()[g]['id']))
        return ids
    raise Exception('Username not found')