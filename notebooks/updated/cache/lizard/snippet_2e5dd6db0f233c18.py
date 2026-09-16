def BFS(G, start):
    if start not in G.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (start,))
    color = {}
    pred = {}
    dist = {}
    queue = Queue()
    queue.put(start)
    for vertex in G.vertices:
        color[vertex] = 'white'
        pred[vertex] = None
        dist[vertex] = 0
    while queue.qsize() > 0:
        current = queue.get()
        for neighbor in G.vertices[current]:
            if color[neighbor] == 'white':
                color[neighbor] = 'grey'
                pred[neighbor] = current
                dist[neighbor] = dist[current] + 1
                queue.put(neighbor)
        color[current] = 'black'
    return pred