def new(self, name=None, stack='cedar', region=None):
    payload = {}
    if name:
        payload['app[name]'] = name
    if stack:
        payload['app[stack]'] = stack
    if region:
        payload['app[region]'] = region
    r = self._h._http_resource(method='POST', resource=('apps',), data=payload)
    name = json.loads(r.content).get('name')
    return self._h.apps.get(name)