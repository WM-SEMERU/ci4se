def prune_candidates(candidates):
    pruned = []
    for first, second in candidates:
        if first.__class__ is Linearization:
            nodes1 = first.curve.nodes
        else:
            nodes1 = first.nodes
        if second.__class__ is Linearization:
            nodes2 = second.curve.nodes
        else:
            nodes2 = second.nodes
        if convex_hull_collide(nodes1, nodes2):
            pruned.append((first, second))
    return pruned