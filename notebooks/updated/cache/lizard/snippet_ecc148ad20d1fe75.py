def _yarn_node_metrics(self, rm_address, instance, addl_tags):
    metrics_json = self._rest_request_to_json(rm_address, instance,
        YARN_NODES_PATH, addl_tags)
    if metrics_json and metrics_json['nodes'] is not None and metrics_json[
        'nodes']['node'] is not None:
        for node_json in metrics_json['nodes']['node']:
            node_id = node_json['id']
            tags = ['node_id:{}'.format(str(node_id))]
            tags.extend(addl_tags)
            self._set_yarn_metrics_from_json(tags, node_json, YARN_NODE_METRICS
                )