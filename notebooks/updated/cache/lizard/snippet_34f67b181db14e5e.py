def name_parser(name, **kwargs):
    url = gbif_baseurl + 'parser/name'
    if name.__class__ == str:
        name = [name]
    return gbif_POST(url, name, **kwargs)