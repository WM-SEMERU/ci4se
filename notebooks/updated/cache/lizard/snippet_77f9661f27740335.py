def compute_groups_matrix(groups):
    if not groups:
        return None
    num_vars = len(groups)
    unique_group_names = list(OrderedDict.fromkeys(groups))
    number_of_groups = len(unique_group_names)
    indices = dict([(x, i) for i, x in enumerate(unique_group_names)])
    output = np.zeros((num_vars, number_of_groups), dtype=np.int)
    for parameter_row, group_membership in enumerate(groups):
        group_index = indices[group_membership]
        output[parameter_row, group_index] = 1
    return output, unique_group_names