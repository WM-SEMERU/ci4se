def hierarchical_group_items(item_list, groupids_list):
    num_groups = len(groupids_list)
    leaf_type = partial(defaultdict, list)
    if num_groups > 1:
        node_type = leaf_type
        for _ in range(len(groupids_list) - 2):
            node_type = partial(defaultdict, node_type)
        root_type = node_type
    elif num_groups == 1:
        root_type = list
    else:
        raise ValueError('must suply groupids')
    tree = defaultdict(root_type)
    groupid_tuple_list = list(zip(*groupids_list))
    for groupid_tuple, item in zip(groupid_tuple_list, item_list):
        node = tree
        for groupid in groupid_tuple:
            node = node[groupid]
        node.append(item)
    return tree