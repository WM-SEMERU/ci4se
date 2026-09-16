def create(self, name, plugin_name, hadoop_version, description=None,
    cluster_configs=None, node_groups=None, anti_affinity=None, net_id=None,
    default_image_id=None, use_autoconfig=None, shares=None, is_public=None,
    is_protected=None, domain_name=None):
    data = {'name': name, 'plugin_name': plugin_name, 'hadoop_version':
        hadoop_version}
    return self._do_create(data, description, cluster_configs, node_groups,
        anti_affinity, net_id, default_image_id, use_autoconfig, shares,
        is_public, is_protected, domain_name)