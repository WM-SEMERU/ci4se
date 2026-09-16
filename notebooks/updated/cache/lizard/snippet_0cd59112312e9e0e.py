def query_kb_mappings(kbid, sortby='to', key='', value='', match_type='s'):
    query = KnwKBRVAL.query.filter(KnwKBRVAL.id_knwKB == kbid)
    if len(key) > 0:
        if match_type == 's':
            key = '%' + key + '%'
        elif match_type == 'sw':
            key = key + '%'
    else:
        key = '%'
    if len(value) > 0:
        if match_type == 's':
            value = '%' + value + '%'
        elif match_type == 'sw':
            value = value + '%'
    else:
        value = '%'
    query = query.filter(KnwKBRVAL.m_key.like(key), KnwKBRVAL.m_value.like(
        value))
    if sortby == 'from':
        query = query.order_by(KnwKBRVAL.m_key)
    else:
        query = query.order_by(KnwKBRVAL.m_value)
    return query