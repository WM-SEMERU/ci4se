def _get_federation_info(address_or_id, federation_service, fed_type='name'):
    params = {'q': address_or_id, 'type': fed_type}
    r = requests.get(federation_service, params=params)
    if r.status_code == 200:
        return r.json()
    else:
        return None