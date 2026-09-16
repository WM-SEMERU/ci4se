def add_mongo_config_with_uri(app, connection_string_uri, database_name,
    collection_name):
    app.config['data'] = PyMongoDataAccess.build_data_access_with_uri(
        connection_string_uri, database_name, collection_name)