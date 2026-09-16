def load_schema(name):
    data = pkgutil.get_data('jsonschema', 'schemas/{0}.json'.format(name))
    return json.loads(data.decode('utf-8'))