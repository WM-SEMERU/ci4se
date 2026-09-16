def _batched_write_command_compressed(namespace, operation, command, docs,
    check_keys, opts, ctx):
    data, to_send = _encode_batched_write_command(namespace, operation,
        command, docs, check_keys, opts, ctx)
    request_id, msg = _compress(2004, data, ctx.sock_info.compression_context)
    return request_id, msg, to_send