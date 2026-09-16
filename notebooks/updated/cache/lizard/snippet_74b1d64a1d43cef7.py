def fields_to_dtypes(schema):
    datetime_types = ['date', 'datetime']
    datetime_fields = {f['name']: _TABLE_SCHEMA_DTYPE_MAPPING.get(f['type'],
        'object') for f in schema['fields'] if f['type'] in datetime_types}
    other_fields = {f['name']: _TABLE_SCHEMA_DTYPE_MAPPING.get(f['type'],
        'object') for f in schema['fields'] if f['type'] not in datetime_types}
    return {'dates': datetime_fields, 'other': other_fields}