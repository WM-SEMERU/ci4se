def is_type_II_branch(u, v, dfs_data):
    if u != a(v, dfs_data):
        return False
    if u < L2(v, dfs_data):
        return True
    return False