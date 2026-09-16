def _extract_global_operations(ir_blocks_except_output_and_folds):
    global_operation_blocks = []
    remaining_ir_blocks = []
    in_global_operations_scope = False
    for block in ir_blocks_except_output_and_folds:
        if isinstance(block, (ConstructResult, Fold, Unfold)):
            raise AssertionError(
                'Received unexpected block of type {}. No ConstructResult or Fold/Unfold blocks should be present: {}'
                .format(type(block).__name__,
                ir_blocks_except_output_and_folds))
        elif isinstance(block, GlobalOperationsStart):
            in_global_operations_scope = True
        elif in_global_operations_scope:
            global_operation_blocks.append(block)
        else:
            remaining_ir_blocks.append(block)
    return global_operation_blocks, remaining_ir_blocks