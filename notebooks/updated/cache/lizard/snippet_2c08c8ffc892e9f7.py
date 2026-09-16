def get_connector(database_name=None):
    from django.db import connections, DEFAULT_DB_ALIAS
    database_name = database_name or DEFAULT_DB_ALIAS
    connection = connections[database_name]
    engine = connection.settings_dict['ENGINE']
    connector_settings = settings.CONNECTORS.get(database_name, {})
    connector_path = connector_settings.get('CONNECTOR', CONNECTOR_MAPPING[
        engine])
    connector_module_path = '.'.join(connector_path.split('.')[:-1])
    module = import_module(connector_module_path)
    connector_name = connector_path.split('.')[-1]
    connector = getattr(module, connector_name)
    return connector(database_name, **connector_settings)