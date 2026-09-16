def create_zone(server, token, domain, identifier, dtype, master=None):
    method = 'PUT'
    uri = 'https://' + server + '/zone'
    obj = JSONConverter(domain)
    obj.generate_zone(domain, identifier, dtype, master)
    connect.tonicdns_client(uri, method, token, obj.zone)