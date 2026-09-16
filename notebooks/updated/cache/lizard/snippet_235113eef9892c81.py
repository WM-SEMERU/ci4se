def return_file_objects(connection, container, prefix='database'):
    options = []
    meta_data = objectstore.get_full_container_list(connection, container,
        prefix='database')
    env = ENV.upper()
    for o_info in meta_data:
        expected_file = f'database.{ENV}'
        if o_info['name'].startswith(expected_file):
            dt = dateparser.parse(o_info['last_modified'])
            now = datetime.datetime.now()
            delta = now - dt
            LOG.debug('AGE: %d %s', delta.days, expected_file)
            options.append((dt, o_info))
        options.sort()
    return options