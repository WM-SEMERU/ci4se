def GetCollectionNode(self, partition_key):
    if partition_key is None:
        raise ValueError('partition_key is None or empty.')
    partition_number = self._FindPartition(self._GetBytes(partition_key))
    return self.partitions[partition_number].GetNode()