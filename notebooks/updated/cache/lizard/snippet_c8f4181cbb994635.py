def _apply_scratch_as_phase(args: Dict[str, Any]):
    state = _state_shard(args)
    state *= np.exp(I_PI_OVER_2 * _scratch_shard(args))