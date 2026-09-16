def _find_schema(data_path, schema_name):
    path = glob.glob(schema_name)
    for p in path:
        if os.path.isfile(p):
            return p
    return _find_data_path_schema(data_path, schema_name)