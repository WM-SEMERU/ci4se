def create_style(self, title=None, defaults=None, mappings=None, verbose=
    VERBOSE):
    u = self.__url
    host = u.split('//')[1].split(':')[0]
    port = u.split(':')[2].split('/')[0]
    version = u.split(':')[2].split('/')[1]
    if defaults:
        defaults_ = []
        for d in defaults:
            if d:
                defaults_.append(d)
        defaults = defaults_
    if mappings:
        mappings_ = []
        for m in mappings:
            if m:
                mappings_.append(m)
        mappings = mappings_
    try:
        update_style(title=title, defaults=defaults, mappings=mappings,
            host=host, port=port)
        print('Existing style was updated.')
        sys.stdout.flush()
    except:
        print('Creating new style.')
        sys.stdout.flush()
        URL = 'http://' + str(host) + ':' + str(port) + '/v1/styles'
        PARAMS = {'title': title, 'defaults': defaults, 'mappings': mappings}
        r = requests.post(url=URL, json=PARAMS)
        checkresponse(r)