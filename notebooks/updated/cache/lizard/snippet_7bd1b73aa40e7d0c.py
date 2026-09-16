def get_facts(api_url=None, query='', verify=False, cert=list()):
    return utils._make_api_request(api_url, '/facts', verify, cert, params=
        {'query': query})