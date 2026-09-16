def _load(db_data, db):
    if db.name != db_data['name']:
        raise ValueError("dbname doesn't matches! Maybe wrong database data.")
    db.__init__(client=db._client, name=db.name)
    for col_name, col_data in iteritems(db_data['_collections']):
        collection = db.get_collection(col_name)
        collection._documents = col_data['_documents']
        collection._uniques = col_data['_uniques']
        db._collections[col_name] = collection
    return db