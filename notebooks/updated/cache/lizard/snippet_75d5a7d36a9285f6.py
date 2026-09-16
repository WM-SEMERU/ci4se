def vt_hash_check(fhash, vt_api):
    if not is_hash(fhash):
        return None
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    parameters = {'resource': fhash, 'apikey': vt_api}
    response = requests.get(url, params=parameters)
    try:
        return response.json()
    except ValueError:
        return None