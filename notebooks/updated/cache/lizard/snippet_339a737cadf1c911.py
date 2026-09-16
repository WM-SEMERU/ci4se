def get_client(host=None, port=None, username=None, password=None,
    enable_logging=True):
    host = utils.first_true([host, config['bel_api']['servers'][
        'arangodb_host'], 'localhost'])
    port = utils.first_true([port, config['bel_api']['servers'][
        'arangodb_port'], 8529])
    username = utils.first_true([username, config['bel_api']['servers'][
        'arangodb_username'], ''])
    password = utils.first_true([password, config.get('secrets', config[
        'secrets']['bel_api']['servers'].get('arangodb_password')), ''])
    client = arango.client.ArangoClient(protocol=config['bel_api'][
        'servers']['arangodb_protocol'], host=host, port=port)
    return client