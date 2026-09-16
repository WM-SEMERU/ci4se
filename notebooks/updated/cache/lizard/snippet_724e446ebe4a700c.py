def get_preferred_partition(self, broker, sibling_distance):
    eligible_partitions = self.partitions - broker.partitions
    if eligible_partitions:
        pref_partition = min(eligible_partitions, key=lambda
            source_partition: sibling_distance[source_partition.topic])
        return pref_partition
    else:
        return None