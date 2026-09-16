def merge_entity(self, entity, if_match='*'):
    request = _merge_entity(entity, if_match)
    self._add_to_batch(entity['PartitionKey'], entity['RowKey'], request)