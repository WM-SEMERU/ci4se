def group_keys_by_replica(session, keyspace, table, keys):
    cluster = session.cluster
    partition_keys = cluster.metadata.keyspaces[keyspace].tables[table
        ].partition_key
    serializers = list(types._cqltypes[partition_key.cql_type] for
        partition_key in partition_keys)
    keys_per_host = defaultdict(list)
    distance = cluster._default_load_balancing_policy.distance
    for key in keys:
        serialized_key = [serializer.serialize(pk, cluster.protocol_version
            ) for serializer, pk in zip(serializers, key)]
        if len(serialized_key) == 1:
            routing_key = serialized_key[0]
        else:
            routing_key = b''.join(struct.pack('>H%dsB' % len(p), len(p), p,
                0) for p in serialized_key)
        all_replicas = cluster.metadata.get_replicas(keyspace, routing_key)
        valid_replicas = [host for host in all_replicas if host.is_up and 
            distance(host) == HostDistance.LOCAL]
        if not valid_replicas:
            valid_replicas = [host for host in all_replicas if host.is_up]
        if valid_replicas:
            keys_per_host[random.choice(valid_replicas)].append(key)
        else:
            keys_per_host[NO_VALID_REPLICA].append(key)
    return dict(keys_per_host)