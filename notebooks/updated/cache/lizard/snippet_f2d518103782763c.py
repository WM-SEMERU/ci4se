def identify_groups(groups):
    group_ids = np.unique(groups)
    num_groups = len(group_ids)
    if num_groups < 2:
        raise ValueError(
            'There must be atleast two nodes or groups in data, for pair-wise edge-weight calculations.'
            )
    return group_ids, num_groups