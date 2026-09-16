def CreateUserDefinedFunction(self, collection_link, udf, options=None):
    if options is None:
        options = {}
    collection_id, path, udf = self._GetContainerIdWithPathForUDF(
        collection_link, udf)
    return self.Create(udf, path, 'udfs', collection_id, None, options)