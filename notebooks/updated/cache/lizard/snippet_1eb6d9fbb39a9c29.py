def _per_location_tuple_to_step(ir_tuple):
    root_block = ir_tuple[0]
    if not isinstance(root_block, root_block_types):
        raise AssertionError('Unexpected root block type for MatchStep: {} {}'
            .format(root_block, ir_tuple))
    coerce_type_block = None
    where_block = None
    as_block = None
    for block in ir_tuple[1:]:
        if isinstance(block, CoerceType):
            if coerce_type_block is not None:
                raise AssertionError(
                    'Unexpectedly found two blocks eligible for "class" clause: {} {} {}'
                    .format(block, coerce_type_block, ir_tuple))
            coerce_type_block = block
        elif isinstance(block, MarkLocation):
            if as_block is not None:
                raise AssertionError(
                    'Unexpectedly found two blocks eligible for "as" clause: {} {} {}'
                    .format(block, as_block, ir_tuple))
            as_block = block
        elif isinstance(block, Filter):
            if where_block is not None:
                raise AssertionError(
                    'Unexpectedly found two blocks eligible for "where" clause: {} {} {}'
                    .format(block, as_block, ir_tuple))
            if as_block is not None:
                raise AssertionError(
                    'Unexpectedly found MarkLocation before Filter in MatchStep: {} {} {}'
                    .format(block, where_block, ir_tuple))
            where_block = block
        else:
            raise AssertionError('Unexpected block encountered: {} {}'.
                format(block, ir_tuple))
    step = MatchStep(root_block=root_block, coerce_type_block=
        coerce_type_block, where_block=where_block, as_block=as_block)
    if isinstance(root_block, Backtrack):
        if where_block is not None or coerce_type_block is not None:
            raise AssertionError(
                'Unexpected blocks in Backtrack-based MatchStep: {}'.format
                (step))
    return step