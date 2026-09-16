def _pmap(self, func, items, keys, pool, bookkeeping_dict=None):
    if keys is not None:
        key_indices = _duplicates(keys).values()
    else:
        key_indices = [[i] for i in range(len(items))]
    if pool is not None:
        results = pool.map(functools.partial(_unpickle_run, pickle.dumps(
            func)), [items[i[0]] for i in key_indices])
    else:
        results = map(func, [items[i[0]] for i in key_indices])
    if bookkeeping_dict is not None:
        bookkeeping_dict['key_indices'] = key_indices
    all_results = [None] * len(items)
    for indices, result in zip(key_indices, results):
        for j, i in enumerate(indices):
            if j > 0:
                result = copy.deepcopy(result)
            all_results[i] = result
    return all_results