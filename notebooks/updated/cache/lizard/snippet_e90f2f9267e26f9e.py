def collection_updated_percolator(mapper, connection, target):
    delete_collection_percolator(target)
    if target.dbquery is not None:
        new_collection_percolator(target)