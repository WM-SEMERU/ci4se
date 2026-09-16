def get_org_details(organization_id):
    qdata = salt.utils.http.query('{0}/organization/{1}'.format(_base_url(),
        organization_id), method='GET', decode=True, decode_type='json',
        header_dict={'X-DC-DEVKEY': _api_key(), 'Content-Type':
        'application/json'})
    return qdata