def citation_count(doi, url='http://www.crossref.org/openurl/', key=
    'cboettig@ropensci.org', **kwargs):
    args = {'id': 'doi:' + doi, 'pid': key, 'noredirect': True}
    args = dict((k, v) for k, v in args.items() if v)
    res = requests.get(url, params=args, headers=make_ua(), **kwargs)
    xmldoc = minidom.parseString(res.content)
    val = xmldoc.getElementsByTagName('query')[0].attributes['fl_count'].value
    return int(str(val))