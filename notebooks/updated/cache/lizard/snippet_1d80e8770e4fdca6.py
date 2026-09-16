def _get_field_mapping(self, schema):
    if 'mapping' in schema:
        return schema['mapping']
    elif schema['type'] == 'dict' and 'schema' in schema:
        return self._get_mapping(schema['schema'])
    elif schema['type'] == 'list' and 'schema' in schema.get('schema', {}):
        return self._get_mapping(schema['schema']['schema'])
    elif schema['type'] == 'datetime':
        return {'type': 'date'}
    elif schema['type'] == 'string' and schema.get('unique'):
        return {'type': 'string', 'index': 'not_analyzed'}