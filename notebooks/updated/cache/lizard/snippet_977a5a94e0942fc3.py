def get_record_collections(record, matcher):
    collections = current_collections.collections
    if collections is None:
        collections = current_collections.collections = dict(_build_cache())
    output = set()
    for collections in matcher(collections, record):
        output |= collections
    return list(output)