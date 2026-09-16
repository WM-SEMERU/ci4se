def update_meta_data(meta=None):
    if meta is None:
        meta = {}
    if 'DATE' not in meta:
        meta['DATE'] = strftime('%Y-%m-%d %H:%M:%S', gmtime())
    if 'PROGRAM' not in meta:
        meta['PROGRAM'] = 'AegeanTools.catalogs'
        meta['PROGVER'] = '{0}-({1})'.format(__version__, __date__)
    return meta