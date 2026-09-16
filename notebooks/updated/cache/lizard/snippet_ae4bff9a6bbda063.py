def get_data(dataset, query=None, crs='epsg:4326', bounds=None, sortby=None,
    pagesize=10000, max_workers=5):
    param_dicts = define_request(dataset, query, crs, bounds, sortby, pagesize)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(make_request, param_dicts)
    outjson = dict(type='FeatureCollection', features=[])
    for result in results:
        outjson['features'] += result
    return outjson