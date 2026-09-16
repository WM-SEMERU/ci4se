def db_url_from_hass_config(path):
    config = load_hass_config(path)
    default_path = os.path.join(path, 'home-assistant_v2.db')
    default_url = 'sqlite:///{}'.format(default_path)
    recorder = config.get('recorder')
    if recorder:
        db_url = recorder.get('db_url')
        if db_url is not None:
            return db_url
    if not os.path.isfile(default_path):
        raise ValueError('Unable to determine DB url from hass config at {}'
            .format(path))
    return default_url