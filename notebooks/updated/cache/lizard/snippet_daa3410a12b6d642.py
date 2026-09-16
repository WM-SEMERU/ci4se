def leader_for_partition(self, partition):
    if partition.topic not in self._partitions:
        return None
    elif partition.partition not in self._partitions[partition.topic]:
        return None
    return self._partitions[partition.topic][partition.partition].leader