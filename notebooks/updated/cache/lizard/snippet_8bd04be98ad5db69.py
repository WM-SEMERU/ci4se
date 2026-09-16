def adjustReplicas(self, old_required_number_of_instances: int,
    new_required_number_of_instances: int):
    replica_num = old_required_number_of_instances
    while replica_num < new_required_number_of_instances:
        self.replicas.add_replica(replica_num)
        self.processStashedMsgsForReplica(replica_num)
        replica_num += 1
    while replica_num > new_required_number_of_instances:
        replica_num -= 1
        self.replicas.remove_replica(replica_num)
    pop_keys(self.msgsForFutureReplicas, lambda inst_id: inst_id <
        new_required_number_of_instances)
    if len(self.primaries_disconnection_times
        ) < new_required_number_of_instances:
        self.primaries_disconnection_times.extend([None] * (
            new_required_number_of_instances - len(self.
            primaries_disconnection_times)))
    elif len(self.primaries_disconnection_times
        ) > new_required_number_of_instances:
        self.primaries_disconnection_times = (self.
            primaries_disconnection_times[:new_required_number_of_instances])