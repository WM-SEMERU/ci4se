def build_decryption_materials_cache_key(partition, request):
    hasher = _new_cache_key_hasher()
    _partition_hash = _partition_name_hash(hasher=hasher.copy(),
        partition_name=partition)
    _algorithm_info = request.algorithm.id_as_bytes()
    _edks_hash = _encrypted_data_keys_hash(hasher=hasher.copy(),
        encrypted_data_keys=request.encrypted_data_keys)
    _ec_hash = _encryption_context_hash(hasher=hasher.copy(),
        encryption_context=request.encryption_context)
    hasher.update(_partition_hash)
    hasher.update(_algorithm_info)
    hasher.update(_edks_hash)
    hasher.update(_512_BIT_PAD)
    hasher.update(_ec_hash)
    return hasher.finalize()