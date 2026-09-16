def debug_consec_list(list_):
    if not issorted(list_):
        print('warning list is not sorted. indices will not match')
    sortedlist = sorted(list_)
    start = sortedlist[0]
    last = start - 1
    missing_vals = []
    missing_indices = []
    duplicate_items = []
    for count, item in enumerate(sortedlist):
        diff = item - last
        if diff > 1:
            missing_indices.append(count)
            for miss in range(last + 1, last + diff):
                missing_vals.append(miss)
        elif diff == 0:
            duplicate_items.append(item)
        elif diff == 1:
            pass
        else:
            raise AssertionError('We sorted the list. diff can not be negative'
                )
        last = item
    return missing_vals, missing_indices, duplicate_items