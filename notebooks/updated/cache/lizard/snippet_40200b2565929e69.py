def copy_block(block=None, update_working_block=True):
    block_in = working_block(block)
    block_out, temp_wv_map = _clone_block_and_wires(block_in)
    mems = {}
    for net in block_in.logic:
        _copy_net(block_out, net, temp_wv_map, mems)
    block_out.mem_map = mems
    if update_working_block:
        set_working_block(block_out)
    return block_out