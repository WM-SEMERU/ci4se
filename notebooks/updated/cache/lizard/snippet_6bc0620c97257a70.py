def _resolve(self, path, migration_file):
    variables = {}
    name = '_'.join(migration_file.split('_')[4:])
    migration_file = os.path.join(path, '%s.py' % migration_file)
    with open(migration_file) as fh:
        exec(fh.read(), {}, variables)
    klass = variables[inflection.camelize(name)]
    instance = klass()
    instance.set_schema_builder(self.get_repository().get_connection().
        get_schema_builder())
    return instance