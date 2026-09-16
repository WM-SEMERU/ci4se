def process_data_config_section(config, data_config):
    if 'connectors' in data_config:
        for connector in data_config['connectors']:
            config.data['connectors'][connector['name']
                ] = get_config_from_package(connector['class'])
    if 'sources' in data_config:
        if data_config['sources']:
            for source in data_config['sources']:
                config.data['sources'][source['name']] = source
                del config.data['sources'][source['name']]['name']