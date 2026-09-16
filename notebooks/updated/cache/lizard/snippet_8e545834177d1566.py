def _check_for_batch_clashes(xs):
    names = set([x['description'] for x in xs])
    dups = set([])
    for x in xs:
        batches = tz.get_in(('metadata', 'batch'), x)
        if batches:
            if not isinstance(batches, (list, tuple)):
                batches = [batches]
            for batch in batches:
                if batch in names:
                    dups.add(batch)
    if len(dups) > 0:
        raise ValueError(
            """Batch names must be unique from sample descriptions.
Clashing batch names: %s"""
             % sorted(list(dups)))