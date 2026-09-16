def ordered_covering(routing_table, target_length, aliases=dict(), no_raise
    =False):
    aliases = dict(aliases)
    routing_table = sorted(routing_table, key=lambda entry: _get_generality
        (entry.key, entry.mask))
    while target_length is None or len(routing_table) > target_length:
        merge = _get_best_merge(routing_table, aliases)
        if merge.goodness <= 0:
            break
        routing_table, aliases = merge.apply(aliases)
    if not no_raise and target_length is not None and len(routing_table
        ) > target_length:
        raise MinimisationFailedError(target_length, len(routing_table))
    return routing_table, aliases