def ResolveForCreate(self, document):
    if document is None:
        raise ValueError('document is None.')
    partition_key = self.partition_key_extractor(document)
    return self.consistent_hash_ring.GetCollectionNode(partition_key)