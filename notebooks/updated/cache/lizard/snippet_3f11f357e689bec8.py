def get_schema(repo, content_type):
    try:
        with open(os.path.join(repo.working_dir, '_schemas', '%s.avsc' % (
            content_type,)), 'r') as fp:
            data = fp.read()
            return avro.schema.parse(data)
    except IOError:
        raise NotFound('Schema does not exist.')