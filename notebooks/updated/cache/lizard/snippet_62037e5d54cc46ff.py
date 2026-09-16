def _send_dweet(payload, url, params=None, session=None):
    data = json.dumps(payload)
    headers = {'Content-type': 'application/json'}
    return _request('post', url, data=data, headers=headers, params=params,
        session=session)