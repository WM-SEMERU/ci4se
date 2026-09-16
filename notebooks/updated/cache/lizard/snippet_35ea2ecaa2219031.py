def get_field_list(fields, schema):
    if schema:
        all_fields = [f['name'] for f in schema._bq_schema if f['type'] !=
            'RECORD']
    if isinstance(fields, list):
        if schema:
            for f in fields:
                if f not in all_fields:
                    raise Exception('Cannot find field %s in given schema' % f)
        return fields
    if isinstance(fields, basestring) and fields != '*':
        if schema:
            for f in fields.split(','):
                if f not in all_fields:
                    raise Exception('Cannot find field %s in given schema' % f)
            return fields.split(',')
    if not schema:
        return []
    return all_fields