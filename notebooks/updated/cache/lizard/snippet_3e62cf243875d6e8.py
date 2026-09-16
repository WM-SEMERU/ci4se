def finalize(state, block):
    if state.is_METROPOLIS():
        br = state.config['BYZANTIUM_BLOCK_REWARD']
        nr = state.config['BYZANTIUM_NEPHEW_REWARD']
    else:
        br = state.config['BLOCK_REWARD']
        nr = state.config['NEPHEW_REWARD']
    delta = int(br + nr * len(block.uncles))
    state.delta_balance(state.block_coinbase, delta)
    udpf = state.config['UNCLE_DEPTH_PENALTY_FACTOR']
    for uncle in block.uncles:
        r = int(br * (udpf + uncle.number - state.block_number) // udpf)
        state.delta_balance(uncle.coinbase, r)
    if state.block_number - state.config['MAX_UNCLE_DEPTH'
        ] in state.recent_uncles:
        del state.recent_uncles[state.block_number - state.config[
            'MAX_UNCLE_DEPTH']]