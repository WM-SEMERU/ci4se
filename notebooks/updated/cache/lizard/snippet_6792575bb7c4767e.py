def _get_best_merge(routing_table, aliases):
    best_merge = _Merge(routing_table)
    best_goodness = 0
    for merge in _get_all_merges(routing_table):
        if merge.goodness <= best_goodness:
            continue
        merge = _refine_merge(merge, aliases, min_goodness=best_goodness)
        if merge.goodness > best_goodness:
            best_merge = merge
            best_goodness = merge.goodness
    return best_merge