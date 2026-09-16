def _bfs_from_cluster_tree(tree, bfs_root):
    result = []
    to_process = [bfs_root]
    while to_process:
        result.extend(to_process)
        to_process = tree['child'][np.in1d(tree['parent'], to_process)].tolist(
            )
    return result