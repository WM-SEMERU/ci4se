def DFS_Tree(G):
    if not G.vertices:
        raise GraphInsertError('This graph have no vertices.')
    pred = {}
    T = digraph.DiGraph()
    vertex_data = DFS(G)
    for vertex in vertex_data:
        pred[vertex] = vertex_data[vertex][0]
    queue = Queue()
    for vertex in pred:
        if pred[vertex] == None:
            queue.put(vertex)
    while queue.qsize() > 0:
        current = queue.get()
        for element in pred:
            if pred[element] == current:
                T.add_edge(current, element)
                queue.put(element)
    return T