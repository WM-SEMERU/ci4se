def minimise_tables(routing_tables, target_lengths, methods=(
    remove_default_entries, ordered_covering)):
    if not isinstance(target_lengths, dict):
        lengths = collections.defaultdict(lambda : target_lengths)
    else:
        lengths = target_lengths
    new_tables = dict()
    for chip, table in iteritems(routing_tables):
        try:
            new_table = minimise_table(table, lengths[chip], methods)
        except MinimisationFailedError as exc:
            exc.chip = chip
            raise
        if new_table:
            new_tables[chip] = new_table
    return new_tables