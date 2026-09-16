def query_tracking_code(tracking_code, year=None):
    payload = {'Anio': year or datetime.now().year, 'Tracking': tracking_code}
    response = _make_request(TRACKING_URL, payload)
    if not response['d']:
        return []
    data = response['d'][0]
    destination = data['RetornoCadena6']
    payload.update({'Destino': destination})
    response = _make_request(TRACKING_DETAIL_URL, payload)
    return _process_detail(response['d'])