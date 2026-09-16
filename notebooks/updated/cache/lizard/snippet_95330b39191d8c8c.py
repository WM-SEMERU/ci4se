def load_clients(stream, configuration_class=ClientConfiguration):
    client_dict = yaml.safe_load(stream)
    if isinstance(client_dict, dict):
        return {client_name: configuration_class(**client_config) for 
            client_name, client_config in six.iteritems(client_dict)}
    raise ValueError('Valid configuration could not be decoded.')