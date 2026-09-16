def avatar_url_from_email(email, size=64, default='retro', dns=False):
    if dns:
        import libravatar
        return libravatar.libravatar_url(email=email, size=size, default=
            default)
    else:
        params = _ordered_query_params([('s', size), ('d', default)])
        query = parse.urlencode(params)
        hash = md5(email.encode('utf-8')).hexdigest()
        return 'https://seccdn.libravatar.org/avatar/%s?%s' % (hash, query)