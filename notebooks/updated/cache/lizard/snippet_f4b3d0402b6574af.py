def _validate_all_blocks_supported(ir_blocks, query_metadata_table):
    if len(ir_blocks) < 3:
        raise AssertionError(
            'Unexpectedly attempting to validate IR blocks with fewer than 3 blocks. A minimal query is expected to have at least a QueryRoot, GlobalOperationsStart, and ConstructResult block. The query metadata table is {}.'
            .format(query_metadata_table))
    construct_result = _get_construct_result(ir_blocks)
    unsupported_blocks = []
    unsupported_fields = []
    for block in ir_blocks[:-1]:
        if isinstance(block, constants.SUPPORTED_BLOCK_TYPES):
            continue
        if isinstance(block, constants.SKIPPABLE_BLOCK_TYPES):
            continue
        unsupported_blocks.append(block)
    for field_name, field in six.iteritems(construct_result.fields):
        if not isinstance(field, constants.SUPPORTED_OUTPUT_EXPRESSION_TYPES):
            unsupported_fields.append((field_name, field))
        elif field.location.field in constants.UNSUPPORTED_META_FIELDS:
            unsupported_fields.append((field_name, field))
    if len(unsupported_blocks) > 0 or len(unsupported_fields) > 0:
        raise NotImplementedError(
            'Encountered unsupported blocks {} and unsupported fields {} during construction of SQL query tree for IR blocks {} with query metadata table {}.'
            .format(unsupported_blocks, unsupported_fields, ir_blocks,
            query_metadata_table))