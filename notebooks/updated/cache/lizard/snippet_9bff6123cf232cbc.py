def get_collection_documents_generator(client, database_name,
    collection_name, spec, latest_n, sort_key):
    mongo_database = client[database_name]
    collection = mongo_database[collection_name]
    collection.create_index(sort_key)
    if latest_n is not None:
        skip_n = collection.count() - latest_n
        if collection.count() - latest_n < 0:
            skip_n = 0
        cursor = collection.find(filter=spec).sort([(sort_key, ASCENDING)])
        cursor = cursor[skip_n:]
    else:
        cursor = collection.find(filter=spec).sort([(sort_key, ASCENDING)])
    for document in cursor:
        yield document