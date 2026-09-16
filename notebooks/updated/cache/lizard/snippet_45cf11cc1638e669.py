def nearest_point(query, root_id, get_properties, dist_fun=euclidean_dist):
    k = len(query)
    dist = math.inf
    nearest_node_id = None
    stack_node = deque([root_id])
    stack_look = deque()
    while stack_node or stack_look:
        if stack_node:
            node_id = stack_node.pop()
            look_node = False
        else:
            node_id = stack_look.pop()
            look_node = True
        point, region, axis, active, left, right = get_properties(node_id)
        if look_node:
            inside_region = True
            for i in range(k):
                inside_region &= interval_condition(query[i], region[i][0],
                    region[i][1], dist)
            if not inside_region:
                continue
        if active:
            node_distance = dist_fun(query, point)
            if nearest_node_id is None or dist > node_distance:
                nearest_node_id = node_id
                dist = node_distance
        if query[axis] < point[axis]:
            side_node = left
            side_look = right
        else:
            side_node = right
            side_look = left
        if side_node is not None:
            stack_node.append(side_node)
        if side_look is not None:
            stack_look.append(side_look)
    return nearest_node_id, dist