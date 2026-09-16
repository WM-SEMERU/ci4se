def _a_star_search_internal(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}
    goal_reached = False
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            goal_reached = True
            break
        for next_node in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.edge_cost(current,
                next_node)
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node
                ]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(goal, next_node)
                frontier.put(next_node, priority)
                came_from[next_node] = current
    return came_from, cost_so_far, goal_reached