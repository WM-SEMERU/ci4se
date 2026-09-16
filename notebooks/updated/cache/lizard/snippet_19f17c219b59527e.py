def resolve(self, from_email):
    if from_email is None or not isinstance(from_email, six.string_types):
        raise MissingFromEmail(from_email)
    parent_incident_id = self['incident']['id']
    endpoint_format = 'incidents/{0}/alerts/{1}'
    endpoint = endpoint_format.format(parent_incident_id, self['id'])
    add_headers = {'from': from_email}
    data = {'alert': {'id': self['id'], 'type': 'alert', 'status': 'resolved'}}
    result = self.request('PUT', endpoint=endpoint, add_headers=add_headers,
        data=data)
    return result