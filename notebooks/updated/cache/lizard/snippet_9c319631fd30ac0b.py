def dfs(graph, func, head, reverse=None):
    todo = deque()
    todo.append(head)
    path = deque()
    done = set()
    while todo:
        node = todo.popleft()
        if node in done:
            path.pop()
            continue
        done.add(node)
        path.append(node)
        result = func(node, path, graph)
        if result:
            if reverse:
                children = graph.get_parents(node)
            else:
                children = graph.get_children(node)
            todo.extend(children)