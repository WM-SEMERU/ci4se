def _list_records(self, rtype=None, name=None, content=None):
    opts = {'domain': self._domain}
    if rtype is not None:
        opts['type'] = rtype.upper()
    if name is not None:
        opts['name'] = self._full_name(name)
    if content is not None:
        opts['content'] = content
    opts.update(self._auth)
    response = self._api.nameserver.info(opts)
    self._validate_response(response=response, message='Failed to get records')
    records = []
    if 'record' in response['resData']:
        for record in response['resData']['record']:
            processed_record = {'type': record['type'], 'name': record[
                'name'], 'ttl': record['ttl'], 'content': record['content'],
                'id': record['id']}
            records.append(processed_record)
    return records