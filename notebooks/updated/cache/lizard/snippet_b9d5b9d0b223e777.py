def get(self, workflow_id):
    try:
        db = self._client[self.database]
        fs = GridFSProxy(GridFS(db.unproxied_object))
        return DataStoreDocument(db[WORKFLOW_DATA_COLLECTION_NAME], fs,
            workflow_id)
    except ConnectionFailure:
        raise DataStoreNotConnected()