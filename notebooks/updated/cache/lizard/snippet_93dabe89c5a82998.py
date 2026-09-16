def create(self, identity_id, service, total_allowance=None,
    analyze_queries=None):
    params = {'service': service}
    if total_allowance is not None:
        params['total_allowance'] = total_allowance
    if analyze_queries is not None:
        params['analyze_queries'] = analyze_queries
    return self.request.post(str(identity_id) + '/limit/', params)