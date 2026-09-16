def mongodb_ensure_index(database_name, collection_name, key):
    try:
        mongodb_client_url = getattr(settings, 'MONGODB_CLIENT',
            'mongodb://localhost:27017/')
        mc = MongoClient(mongodb_client_url, document_class=OrderedDict)
        dbs = mc[database_name]
        dbc = dbs[collection_name]
        dbc.ensure_index(key)
        return key
    except:
        return str(sys.exc_info())