def get_object_by_record(record):
    if not record:
        return None
    if record.get('uid'):
        return get_object_by_uid(record['uid'])
    if record.get('path'):
        return get_object_by_path(record['path'])
    if record.get('parent_path') and record.get('id'):
        path = '/'.join([record['parent_path'], record['id']])
        return get_object_by_path(path)
    logger.warn("get_object_by_record::No object found! record='%r'" % record)
    return None