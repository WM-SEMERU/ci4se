def list_schemas(repo):
    schema_files = glob.glob(os.path.join(repo.working_dir, '_schemas',
        '*.avsc'))
    schemas = {}
    for schema_file in schema_files:
        with open(schema_file, 'r') as fp:
            schema = json.load(fp)
            schemas['%(namespace)s.%(name)s' % schema] = schema
    return schemas