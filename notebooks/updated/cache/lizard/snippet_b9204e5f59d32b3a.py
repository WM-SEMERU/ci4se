def get_collectors(self, limit=1000, offset=0):
    options = {'limit': limit, 'offset': offset}
    request = requests.get(self.url, params=options, auth=self.auth)
    try:
        results = request.json()['collectors']
    except KeyError:
        results = request.json()
    except json.decoder.JSONDecodeError:
        results = []
    return results