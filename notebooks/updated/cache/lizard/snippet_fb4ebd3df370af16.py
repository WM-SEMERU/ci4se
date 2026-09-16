def _iterbfs(self, start, end=None, forward=True):
    queue, visited = deque([(start, 0)]), set([start])
    if forward:
        get_edges = self.out_edges
        get_next = self.tail
    else:
        get_edges = self.inc_edges
        get_next = self.head
    while queue:
        curr_node, curr_step = queue.popleft()
        yield curr_node, curr_step
        if curr_node == end:
            break
        for edge in get_edges(curr_node):
            tail = get_next(edge)
            if tail not in visited:
                visited.add(tail)
                queue.append((tail, curr_step + 1))