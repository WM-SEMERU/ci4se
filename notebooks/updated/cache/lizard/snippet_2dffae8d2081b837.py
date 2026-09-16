def _restore_dropped_levels_multijoin(left, right, dropped_level_names,
    join_index, lindexer, rindexer):

    def _convert_to_mulitindex(index):
        if isinstance(index, MultiIndex):
            return index
        else:
            return MultiIndex.from_arrays([index.values], names=[index.name])
    join_index = _convert_to_mulitindex(join_index)
    join_levels = join_index.levels
    join_codes = join_index.codes
    join_names = join_index.names
    if lindexer is None:
        lindexer = range(left.size)
    if rindexer is None:
        rindexer = range(right.size)
    for dropped_level_name in dropped_level_names:
        if dropped_level_name in left.names:
            idx = left
            indexer = lindexer
        else:
            idx = right
            indexer = rindexer
        name_idx = idx.names.index(dropped_level_name)
        restore_levels = idx.levels[name_idx]
        codes = idx.codes[name_idx]
        restore_codes = algos.take_nd(codes, indexer, fill_value=-1)
        join_levels = join_levels + [restore_levels]
        join_codes = join_codes + [restore_codes]
        join_names = join_names + [dropped_level_name]
    return join_levels, join_codes, join_names