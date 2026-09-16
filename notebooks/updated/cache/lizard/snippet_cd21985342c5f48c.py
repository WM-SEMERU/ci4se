def _traverse_report(data):
    if 'items' not in data:
        return {}
    out = {}
    for item in data['items']:
        skip = item['severity'] == 'NonDisplay' or item['itemKey'
            ] == 'categoryDesc' or item['value'] in [None, 'Null', 'N/A',
            'NULL']
        if skip:
            continue
        value = 'Ok' if item['value'] == '0.0' else item['value']
        out[item['itemKey']] = value
        out.update(_traverse_report(item))
    return out