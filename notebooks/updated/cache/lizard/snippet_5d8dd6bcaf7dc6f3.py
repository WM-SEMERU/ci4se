def _load_schema(name, path=__file__):
    path = os.path.join(os.path.dirname(path), name + '.yaml')
    with open(path) as handle:
        schema = yaml.safe_load(handle)
    fast_schema = rapidjson.Validator(rapidjson.dumps(schema))
    return path, (schema, fast_schema)