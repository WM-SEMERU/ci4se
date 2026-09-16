def extract_macaroons(headers_or_request):

    def get_header(key, default=None):
        try:
            return headers_or_request.get_header(key, default)
        except AttributeError:
            return headers_or_request.get(key, default)
    mss = []

    def add_macaroon(data):
        try:
            data = utils.b64decode(data)
            data_as_objs = json.loads(data.decode('utf-8'))
        except ValueError:
            return
        ms = [utils.macaroon_from_dict(x) for x in data_as_objs]
        mss.append(ms)
    cookie_header = get_header('Cookie')
    if cookie_header is not None:
        cs = SimpleCookie()
        cs.load(str(cookie_header))
        for c in cs:
            if c.startswith('macaroon-'):
                add_macaroon(cs[c].value)
    macaroon_header = get_header('Macaroons')
    if macaroon_header is not None:
        for h in macaroon_header.split(','):
            add_macaroon(h)
    return mss