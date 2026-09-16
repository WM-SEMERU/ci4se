def UpsertStoredProcedure(self, collection_link, sproc, options=None):
    if options is None:
        options = {}
    collection_id, path, sproc = self._GetContainerIdWithPathForSproc(
        collection_link, sproc)
    return self.Upsert(sproc, path, 'sprocs', collection_id, None, options)