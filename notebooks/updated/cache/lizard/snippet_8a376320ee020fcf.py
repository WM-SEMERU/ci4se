def make_url(contents, domain=DEFAULT_DOMAIN, force_gist=False,
    size_for_gist=MAX_URL_LEN):
    contents = make_geojson(contents)
    if len(contents) <= size_for_gist and not force_gist:
        url = data_url(contents, domain)
    else:
        gist = _make_gist(contents)
        url = gist_url(gist.id, domain)
    return url