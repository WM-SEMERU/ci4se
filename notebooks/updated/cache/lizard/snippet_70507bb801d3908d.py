def update_records(self, domain, records):
    if not isinstance(records, list):
        raise TypeError('Expected records of type list')
    uri = '/domains/%s/records' % utils.get_id(domain)
    resp, resp_body = self._async_call(uri, method='PUT', body={'records':
        records}, error_class=exc.DomainRecordUpdateFailed, has_response=False)
    return resp_body