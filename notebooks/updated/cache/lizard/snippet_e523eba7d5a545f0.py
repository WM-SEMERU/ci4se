def get_one_ping_per_client(pings):
    if isinstance(pings.first(), binary_type):
        pings = pings.map(lambda p: json.loads(p.decode('utf-8')))
    filtered = pings.filter(lambda p: 'clientID' in p or 'clientId' in p)
    if not filtered:
        raise ValueError('Missing clientID/clientId attribute.')
    if 'clientID' in filtered.first():
        client_id = 'clientID'
    else:
        client_id = 'clientId'
    return filtered.map(lambda p: (p[client_id], p)).reduceByKey(lambda p1,
        p2: p1).map(lambda p: p[1])