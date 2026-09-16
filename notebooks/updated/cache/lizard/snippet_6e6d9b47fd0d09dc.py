def dataproc(cls, graph, data):
    for thing in data:
        graph.add_trip(*thing)
    raise NotImplementedError('You need to implement this yourlself!')