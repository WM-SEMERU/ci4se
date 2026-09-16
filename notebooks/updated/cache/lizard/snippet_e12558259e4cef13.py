def update_record(self, domain, recordid, params=None):
    params = update_params(params, {'domain': domain, 'RECORDID': recordid})
    return self.request('/v1/dns/update_record', params, 'POST')