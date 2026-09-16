def _sanity_check_mark_location_preceding_optional_traverse(ir_blocks):
    _, new_ir_blocks = extract_folds_from_ir_blocks(ir_blocks)
    for first_block, second_block in pairwise(new_ir_blocks):
        if isinstance(second_block, Traverse) and second_block.optional:
            if not isinstance(first_block, MarkLocation):
                raise AssertionError(
                    'Expected MarkLocation before Traverse with optional=True, but none was found: {}'
                    .format(ir_blocks))