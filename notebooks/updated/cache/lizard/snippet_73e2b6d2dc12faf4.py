def _dump(db):
    db_data = {'name': db.name, '_collections': dict()}
    for col_name, collection in iteritems(db._collections):
        if col_name != 'system.indexes':
            col_data = {'_documents': collection._documents, '_uniques':
                collection._uniques}
            db_data['_collections'][col_name] = col_data
    return db_data