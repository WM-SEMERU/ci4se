def edit_page(id, name, space, content):
    data = {}
    data['id'] = str(id)
    data['type'] = 'page'
    data['title'] = name
    data['space'] = {'key': space}
    data['body'] = {'storage': {'value': content, 'representation': 'storage'}}
    data['version'] = {'number': 1}
    response = _api.rest('/' + str(id), 'PUT', _json.dumps(data))
    new_version = int(_json.loads(response)['message'].split()[-1]) + 1
    data['version']['number'] = new_version
    return _api.rest('/' + str(id), 'PUT', _json.dumps(data))