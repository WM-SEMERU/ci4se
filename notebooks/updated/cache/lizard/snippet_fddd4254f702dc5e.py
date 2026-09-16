def collection(self, *collection_path):
    if len(collection_path) == 1:
        path = collection_path[0].split(_helpers.DOCUMENT_PATH_DELIMITER)
    else:
        path = collection_path
    return CollectionReference(*path, client=self)