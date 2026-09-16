def update_entity(self, entity, if_match='*'):
    request = _update_entity(entity, if_match, self._require_encryption,
        self._key_encryption_key, self._encryption_resolver)
    self._add_to_batch(entity['PartitionKey'], entity['RowKey'], request)