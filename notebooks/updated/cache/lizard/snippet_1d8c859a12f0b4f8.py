def read_batch_from_datastore(self, class_batch_id):
    client = self._datastore_client
    key = client.key(KIND_CLASSIFICATION_BATCH, class_batch_id)
    result = client.get(key)
    if result is not None:
        return dict(result)
    else:
        raise KeyError('Key {0} not found in the datastore'.format(key.
            flat_path))