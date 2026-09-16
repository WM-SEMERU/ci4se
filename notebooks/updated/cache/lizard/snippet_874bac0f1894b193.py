def assortativity_indicators(user):
    matrix = matrix_undirected_unweighted(user)
    count_indicator = defaultdict(int)
    total_indicator = defaultdict(int)
    ego_indics = all(user, flatten=True)
    ego_indics = {a: value for a, value in ego_indics.items() if a !=
        'name' and a[:11] != 'reporting__' and a[:10] != 'attributes'}
    for i, u_name in enumerate(matrix_index(user)):
        correspondent = user.network.get(u_name, None)
        if correspondent is None or u_name == user.name or matrix[0][i] == 0:
            continue
        neighbor_indics = all(correspondent, flatten=True)
        for a in ego_indics:
            if ego_indics[a] is not None and neighbor_indics[a] is not None:
                total_indicator[a] += 1
                count_indicator[a] += (ego_indics[a] - neighbor_indics[a]) ** 2
    assortativity = {}
    for i in count_indicator:
        assortativity[i] = count_indicator[i] / total_indicator[i]
    return assortativity