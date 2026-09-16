def list_privileges(name, **client_args):
    client = _client(**client_args)
    res = {}
    for item in client.get_list_privileges(name):
        res[item['database']] = item['privilege'].split()[0].lower()
    return res