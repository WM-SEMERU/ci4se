def print_loopy(self, as_url=True):
    init_str = ''
    node_id = 1
    node_list = {}
    for node, data in self.graph.nodes(data=True):
        node_name = data['name']
        nodex = int(500 * numpy.random.rand())
        nodey = int(500 * numpy.random.rand())
        hue = int(5 * numpy.random.rand())
        node_attr = [node_id, nodex, nodey, 1, node_name, hue]
        node_list[node] = node_attr
        node_id += 1
    nodes = list(node_list.values())
    edges = []
    for s, t, data in self.graph.edges(data=True):
        s_id = node_list[s][0]
        t_id = node_list[t][0]
        if data['polarity'] == 'positive':
            pol = 1
        else:
            pol = -1
        edge = [s_id, t_id, 89, pol, 0]
        edges.append(edge)
    labels = []
    components = [nodes, edges, labels]
    model = json.dumps(components, separators=(',', ':'))
    if as_url:
        model = 'http://ncase.me/loopy/v1/?data=' + model
    return model