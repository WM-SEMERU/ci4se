def parse(self, data):
    graph = self._init_graph()
    if 'type' not in data or data['type'] != 'NetworkGraph':
        raise ParserError('Parse error, not a NetworkGraph object')
    required_keys = ['protocol', 'version', 'metric', 'nodes', 'links']
    for key in required_keys:
        if key not in data:
            raise ParserError('Parse error, "{0}" key not found'.format(key))
    self.protocol = data['protocol']
    self.version = data['version']
    self.revision = data.get('revision')
    self.metric = data['metric']
    for node in data['nodes']:
        graph.add_node(node['id'], label=node['label'] if 'label' in node else
            None, local_addresses=node.get('local_addresses', []), **node.
            get('properties', {}))
    for link in data['links']:
        try:
            source = link['source']
            dest = link['target']
            cost = link['cost']
        except KeyError as e:
            raise ParserError('Parse error, "%s" key not found' % e)
        properties = link.get('properties', {})
        graph.add_edge(source, dest, weight=cost, **properties)
    return graph