def create_payload(self):
    payload = super(Subnet, self).create_payload()
    if 'from_' in payload:
        payload['from'] = payload.pop('from_')
    return {'subnet': payload}