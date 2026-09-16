def MetaGraph(self):
    if self._meta_graph is None:
        raise ValueError('There is no metagraph in this EventAccumulator')
    meta_graph = meta_graph_pb2.MetaGraphDef()
    meta_graph.ParseFromString(self._meta_graph)
    return meta_graph