def greedy_max_inden_setcover(candidate_sets_dict, items, max_covers=None):
    uncovered_set = set(items)
    rejected_keys = set()
    accepted_keys = set()
    covered_items_list = []
    while True:
        if max_covers is not None and len(covered_items_list) >= max_covers:
            break
        maxkey = None
        maxlen = -1
        for key, candidate_items in six.iteritems(candidate_sets_dict):
            if key in rejected_keys or key in accepted_keys:
                continue
            lenval = len(candidate_items)
            if uncovered_set.issuperset(candidate_items):
                if lenval > maxlen:
                    maxkey = key
                    maxlen = lenval
            else:
                rejected_keys.add(key)
        if maxkey is None:
            break
        maxval = candidate_sets_dict[maxkey]
        accepted_keys.add(maxkey)
        covered_items_list.append(list(maxval))
        uncovered_set.difference_update(maxval)
    uncovered_items = list(uncovered_set)
    covertup = uncovered_items, covered_items_list, accepted_keys
    return covertup