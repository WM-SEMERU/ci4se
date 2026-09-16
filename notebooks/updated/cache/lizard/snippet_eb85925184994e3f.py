def update(self, params=None, client=c):
    uri = self.parent.uri
    if not params or not self.res:
        self.get_params()
        return
    d = self.payload
    for k, v in params.items():
        m = d['currentConfiguration'][self.parameter_map[k]]['message']
        if isinstance(v, bool) or isinstance(v, str):
            m['value'] = v
        else:
            try:
                m['expression'] = str(v)
            except KeyError:
                m['value'] = str(v)
    res = client.update_configuration(uri.did, uri.wvm, uri.eid, json.dumps(d))
    if res.status_code == 200:
        self.res = res