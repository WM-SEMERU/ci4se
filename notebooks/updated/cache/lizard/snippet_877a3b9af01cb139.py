def execute(self):
    creator = make_creator(self.params.config, storage_path=self.params.storage
        )
    cluster_name = self.params.cluster
    try:
        cluster = creator.load_cluster(cluster_name)
        if self.params.update:
            cluster.update()
    except (ClusterNotFound, ConfigurationError) as ex:
        log.error('Listing nodes from cluster %s: %s', cluster_name, ex)
        return
    if self.params.pretty_json:
        print(json.dumps(cluster, default=dict, indent=4))
    elif self.params.json:
        print(json.dumps(cluster, default=dict))
    else:
        print(cluster_summary(cluster))
        for cls in cluster.nodes:
            print('%s nodes:' % cls)
            print('')
            for node in cluster.nodes[cls]:
                txt = [('    ' + i) for i in node.pprint().splitlines()]
                print('  - ' + '\n'.join(txt)[4:])
                print('')