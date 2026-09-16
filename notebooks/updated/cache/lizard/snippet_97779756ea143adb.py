def semantic_distance(go_id1, go_id2, godag, branch_dist=None):
    return min_branch_length(go_id1, go_id2, godag, branch_dist)