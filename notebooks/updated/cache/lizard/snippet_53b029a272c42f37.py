def nodes(self):
    if not hasattr(self, '_nodes'):
        base_url = '{}/{}'.format(NodeBalancerConfig.api_endpoint,
            NodeBalancerNode.derived_url_path)
        result = self._client._get_objects(base_url, NodeBalancerNode,
            model=self, parent_id=(self.id, self.nodebalancer_id))
        self._set('_nodes', result)
    return self._nodes