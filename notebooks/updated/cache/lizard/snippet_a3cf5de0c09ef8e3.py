def create_keyspace_network_topology(name, dc_replication_map,
    durable_writes=True, connections=None):
    _create_keyspace(name, durable_writes, 'NetworkTopologyStrategy',
        dc_replication_map, connections=connections)