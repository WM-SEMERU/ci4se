def provides_collection_resource(obj):
    if isinstance(obj, type):
        obj = object.__new__(obj)
    return ICollectionResource in provided_by(obj)