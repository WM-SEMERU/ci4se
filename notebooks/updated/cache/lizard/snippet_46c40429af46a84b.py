def write(settings_path, settings_data, merge=True):
    settings_path = Path(settings_path)
    if settings_path.exists() and merge:
        with io.open(str(settings_path), encoding=default_settings.
            ENCODING_FOR_DYNACONF) as open_file:
            object_merge(yaml.full_load(open_file), settings_data)
    with io.open(str(settings_path), 'w', encoding=default_settings.
        ENCODING_FOR_DYNACONF) as open_file:
        yaml.dump(settings_data, open_file)