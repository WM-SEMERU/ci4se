def query_statements(self, query):
    params = {}
    param_keys = ['registration', 'since', 'until', 'limit', 'ascending',
        'related_activities', 'related_agents', 'format', 'attachments']
    for k, v in query.iteritems():
        if v is not None:
            if k == 'agent':
                params[k] = v.to_json(self.version)
            elif k == 'verb' or k == 'activity':
                params[k] = v.id
            elif k in param_keys:
                params[k] = v
    request = HTTPRequest(method='GET', resource='statements')
    request.query_params = params
    lrs_response = self._send_request(request)
    if lrs_response.success:
        lrs_response.content = StatementsResult.from_json(lrs_response.data)
    return lrs_response