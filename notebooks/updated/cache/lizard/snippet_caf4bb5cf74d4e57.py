def _generate_create_dict(record, record_type, data, ttl, **kwargs):
    resource_record = {'host': record, 'data': data, 'ttl': ttl, 'type':
        record_type}
    for key, value in kwargs.items():
        resource_record.setdefault(key, value)
    return resource_record