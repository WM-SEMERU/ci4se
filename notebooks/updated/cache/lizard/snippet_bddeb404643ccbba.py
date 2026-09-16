def Unprotect(protected_stream_id, protected_stream_key, subcon):
    return Switch(protected_stream_id, {'arcfourvariant':
        ARCFourVariantStream(protected_stream_key, subcon), 'salsa20':
        Salsa20Stream(protected_stream_key, subcon), 'chacha20':
        ChaCha20Stream(protected_stream_key, subcon)}, default=subcon)