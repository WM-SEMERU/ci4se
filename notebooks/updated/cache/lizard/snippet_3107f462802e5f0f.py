def key_leaf(self, data, schema, tree):
    key, value = data
    schema_key, schema_value = schema
    enforce(key, schema_key, tree, 'key')