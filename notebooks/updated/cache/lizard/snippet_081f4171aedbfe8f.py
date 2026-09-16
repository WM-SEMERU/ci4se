def get_schema_file(db_version=1, db='mg_core', collection='materials'):
    d = get_schema_dir(db_version=db_version)
    schemafile = '{}.{}.json'.format(db, collection)
    f = open(os.path.join(d, schemafile), 'r')
    return f