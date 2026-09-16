def _single_qubit_accumulate_into_scratch(args: Dict[str, Any]):
    index = args['indices'][0]
    shard_num = args['shard_num']
    half_turns = args['half_turns']
    num_shard_qubits = args['num_shard_qubits']
    scratch = _scratch_shard(args)
    if index >= num_shard_qubits:
        sign = 1 - 2 * _kth_bit(shard_num, index - num_shard_qubits)
        scratch -= half_turns * sign
    else:
        scratch -= half_turns * _pm_vects(args)[index]