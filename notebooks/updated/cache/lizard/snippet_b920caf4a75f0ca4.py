def batch_geocode(self, addresses, **kwargs):
    fields = ','.join(kwargs.pop('fields', []))
    response = self._req('post', verb='geocode', params={'fields': fields},
        data=json.dumps(addresses))
    if response.status_code != 200:
        return error_response(response)
    return LocationCollection(response.json()['results'])