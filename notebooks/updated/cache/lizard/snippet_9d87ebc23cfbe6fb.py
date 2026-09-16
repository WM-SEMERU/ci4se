def add_group(self, groupname):
    url = self._options['server'] + '/rest/api/latest/group'
    x = OrderedDict()
    x['name'] = groupname
    payload = json.dumps(x)
    self._session.post(url, data=payload)
    return True