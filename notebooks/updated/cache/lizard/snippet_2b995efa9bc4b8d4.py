def add_scheduling_block(config, schema_path=None):
    if schema_path is None:
        schema_path = os.path.join(os.path.dirname(__file__), 'sbi_post.json')
    schema = load_schema(schema_path)
    jsonschema.validate(config, schema)
    DB.set('scheduling_block/{}'.format(config['id']), json.dumps(config))
    DB.rpush('scheduling_block_events', json.dumps(dict(type='created', id=
        config['id'])))