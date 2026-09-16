def write_pa11y_config(item):
    config = {'page': {'headers': item['request_headers']}}
    config_file = tempfile.NamedTemporaryFile(mode='w', prefix=
        'pa11y-config-', suffix='.json', delete=False)
    json.dump(config, config_file)
    config_file.close()
    return config_file