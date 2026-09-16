def get_kb_mappings_json(kb_name='', key='', value='', match_type='s',
    limit=None):
    mappings = get_kb_mappings(kb_name, key, value, match_type)
    ret = []
    if limit is None:
        limit = len(mappings)
    for m in mappings[:limit]:
        label = m['value'] or m['key']
        value = m['key'] or m['value']
        ret.append({'label': label, 'value': value})
    return json.dumps(ret)