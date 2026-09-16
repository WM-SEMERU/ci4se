def _copy_scratch_to_state(args: Dict[str, Any]):
    np.copyto(_state_shard(args), _scratch_shard(args))