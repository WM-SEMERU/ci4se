def move_partition_replica(self, under_loaded_rg, eligible_partition):
    source_broker, dest_broker = self._get_eligible_broker_pair(under_loaded_rg
        , eligible_partition)
    if source_broker and dest_broker:
        self.log.debug(
            'Moving partition {p_name} from broker {source_broker} to replication-group:broker {rg_dest}:{dest_broker}'
            .format(p_name=eligible_partition.name, source_broker=
            source_broker.id, dest_broker=dest_broker.id, rg_dest=
            under_loaded_rg.id))
        source_broker.move_partition(eligible_partition, dest_broker)