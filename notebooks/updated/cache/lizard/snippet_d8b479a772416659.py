def get_unspent_outputs(addresses, confirmations=None, limit=None, api_code
    =None):
    if isinstance(addresses, basestring):
        resource = 'unspent?active=' + addresses
    else:
        resource = 'unspent?active=' + '|'.join(addresses)
    if confirmations is not None:
        resource += '&confirmations=' + str(confirmations)
    if limit is not None:
        resource += '&limit=' + str(limit)
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return [UnspentOutput(o) for o in json_response['unspent_outputs']]