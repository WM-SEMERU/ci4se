def get_rdf_es_idx_map(cls, idx_obj):
    idx_name = list(idx_obj)[0]
    es_map = {'index': idx_name, 'body': {'mappings': {}, 'settings': {
        'index': {'analysis': {'analyzer': {'keylower': {'tokenizer':
        'keyword', 'type': 'custom', 'filter': 'lowercase', 'ignore_above':
        256}}}}}}}
    for idx_cls in idx_obj[idx_name]:
        es_map['body']['mappings'][idx_cls.es_defs['kds_esDocType'][0]] = {
            'properties': idx_cls.es_mapping(idx_cls)}
    return es_map