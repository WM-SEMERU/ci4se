def display_partition_imbalance(cluster_topologies):
    broker_ids = list(next(six.itervalues(cluster_topologies)).brokers.keys())
    assert all(set(broker_ids) == set(cluster_topology.brokers.keys()) for
        cluster_topology in six.itervalues(cluster_topologies))
    broker_partition_counts = [stats.get_broker_partition_counts(
        cluster_topology.brokers[broker_id] for broker_id in broker_ids) for
        cluster_topology in six.itervalues(cluster_topologies)]
    broker_weights = [stats.get_broker_weights(cluster_topology.brokers[
        broker_id] for broker_id in broker_ids) for cluster_topology in six
        .itervalues(cluster_topologies)]
    _display_table_title_multicolumn('Partition Count', 'Broker',
        broker_ids, list(cluster_topologies.keys()), broker_partition_counts)
    print('')
    _display_table_title_multicolumn('Partition Weight', 'Broker',
        broker_ids, list(cluster_topologies.keys()), broker_weights)
    for name, bpc, bw in zip(list(cluster_topologies.keys()),
        broker_partition_counts, broker_weights):
        print(
            """
{name}Partition count imbalance: {net_imbalance}
Broker weight mean: {weight_mean}
Broker weight stdev: {weight_stdev}
Broker weight cv: {weight_cv}"""
            .format(name='' if len(cluster_topologies) == 1 else name +
            '\n', net_imbalance=stats.get_net_imbalance(bpc), weight_mean=
            stats.mean(bw), weight_stdev=stats.stdevp(bw), weight_cv=stats.
            coefficient_of_variation(bw)))