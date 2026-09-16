def find_ds_mapping(data_source, es_major_version):
    mappings = {'raw': None, 'enriched': None}
    connectors = get_connectors()
    try:
        raw_klass = connectors[data_source][1]
        enrich_klass = connectors[data_source][2]
    except KeyError:
        print('Data source not found', data_source)
        sys.exit(1)
    backend = raw_klass(None)
    if backend:
        mapping = json.loads(backend.mapping.get_elastic_mappings(
            es_major_version)['items'])
        mappings['raw'] = [mapping, find_general_mappings(es_major_version)]
    backend = enrich_klass(None)
    if backend:
        mapping = json.loads(backend.mapping.get_elastic_mappings(
            es_major_version)['items'])
        mappings['enriched'] = [mapping, find_general_mappings(
            es_major_version)]
    return mappings