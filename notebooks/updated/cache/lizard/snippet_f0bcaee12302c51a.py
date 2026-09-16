def upgrade(cfg):
    db_node = cfg['db']
    old_db_elems = ['host', 'name', 'port', 'pass', 'user', 'dialect']
    has_old_db_elems = [(x in db_node) for x in old_db_elems]
    if any(has_old_db_elems):
        print(
            'Old database configuration found. Converting to new connect_string. This will *not* be stored in the configuration automatically.'
            )
        cfg['db']['connect_string'
            ] = '{dialect}://{user}:{password}@{host}:{port}/{name}'.format(
            dialect=cfg['db']['dialect']['value'], user=cfg['db']['user'][
            'value'], password=cfg['db']['pass']['value'], host=cfg['db'][
            'host']['value'], port=cfg['db']['port']['value'], name=cfg[
            'db']['name']['value'])