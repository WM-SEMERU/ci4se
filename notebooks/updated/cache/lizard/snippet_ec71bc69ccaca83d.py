def state_view_for_block(block_wrapper, state_view_factory):
    state_root_hash = (block_wrapper.state_root_hash if block_wrapper is not
        None else None)
    return state_view_factory.create_view(state_root_hash)