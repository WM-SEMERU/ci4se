def compile_fetch(raw, doi_id):
    fetch_dict = OrderedDict()
    order = {'author': 'author', 'type': 'type', 'identifier': '', 'title':
        'title', 'journal': 'container-title', 'pubYear': '', 'volume':
        'volume', 'publisher': 'publisher', 'page': 'page', 'issue': 'issue'}
    for k, v in order.items():
        try:
            if k == 'identifier':
                fetch_dict[k] = [{'type': 'doi', 'id': doi_id, 'url': 
                    'http://dx.doi.org/' + doi_id}]
            elif k == 'author':
                fetch_dict[k] = compile_authors(raw[v])
            elif k == 'pubYear':
                fetch_dict[k] = compile_date(raw['issued']['date-parts'])
            else:
                fetch_dict[k] = raw[v]
        except KeyError as e:
            pass
    return fetch_dict