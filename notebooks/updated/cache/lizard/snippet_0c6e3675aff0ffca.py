def create_issue(self, fields=None, prefetch=True, **fieldargs):
    data = _field_worker(fields, **fieldargs)
    p = data['fields']['project']
    if isinstance(p, string_types) or isinstance(p, integer_types):
        data['fields']['project'] = {'id': self.project(p).id}
    p = data['fields']['issuetype']
    if isinstance(p, integer_types):
        data['fields']['issuetype'] = {'id': p}
    if isinstance(p, string_types) or isinstance(p, integer_types):
        data['fields']['issuetype'] = {'id': self.issue_type_by_name(p).id}
    url = self._get_url('issue')
    r = self._session.post(url, data=json.dumps(data))
    raw_issue_json = json_loads(r)
    if 'key' not in raw_issue_json:
        raise JIRAError(r.status_code, response=r, url=url, text=json.dumps
            (data))
    if prefetch:
        return self.issue(raw_issue_json['key'])
    else:
        return Issue(self._options, self._session, raw=raw_issue_json)