def split_and_sort(self):
    graphs = list(self.split())
    graphs.sort(key=lambda x: -len(x.metadata))
    for index, graph in enumerate(graphs):
        graph.index = index
    return graphs