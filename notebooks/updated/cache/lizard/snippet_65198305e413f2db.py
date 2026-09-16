def write_single_batch_images_to_datastore(self, batch_id):
    client = self._datastore_client
    with client.no_transact_batch() as client_batch:
        self._write_single_batch_images_internal(batch_id, client_batch)