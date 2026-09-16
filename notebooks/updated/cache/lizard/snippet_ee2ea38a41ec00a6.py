def find_server(region='EU-London', mode=None):
    if mode:
        region = '%s:%s' % (region, mode)
    opener = urllib.request.build_opener()
    opener.addheaders = default_headers
    data = '%s\n%s' % (region, handshake_version)
    return opener.open('http://m.agar.io/', data=data.encode()).read().decode(
        ).split('\n')[0:2]