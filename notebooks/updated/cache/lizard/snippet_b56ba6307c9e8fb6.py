def workaround_lowering_pass(ir_blocks, query_metadata_table):
    new_ir_blocks = []
    for block in ir_blocks:
        if isinstance(block, Filter):
            new_block = _process_filter_block(query_metadata_table, block)
        else:
            new_block = block
        new_ir_blocks.append(new_block)
    return new_ir_blocks